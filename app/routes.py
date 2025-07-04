from flask import Blueprint, render_template, request, redirect, url_for, flash, session
import json
import random
from datetime import datetime
from app import db
from app.models import Product, CartItem, User, Order
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from .forms import RegisterForm, LoginForm

main = Blueprint("main", __name__)

# Home page
@main.route("/")
def home():
    products = Product.query.all()
    if not products:
        products = [
            {"id": 1, "name": "Echo Dot (5th Gen)", "price": 4499, "image": "echo_dot.jpg"},
            {"id": 2, "name": "Fire TV Stick 4K", "price": 5999, "image": "fire_tv_stick.jpg"},
            {"id": 3, "name": "Noise Smartwatch", "price": 2999, "image": "smartwatch.jpg"},
            {"id": 4, "name": "boAt Rockerz Headphones", "price": 1999, "image": "boat_headphones.jpg"},
            {"id": 5, "name": "HP Wireless Mouse", "price": 799, "image": "hp_mouse.jpg"},
            {"id": 6, "name": "Samsung SSD 1TB", "price": 7499, "image": "samsung_ssd.jpg"},
        ]
    return render_template("index.html", products=products)

# Product detail
@main.route("/product/<int:product_id>")
def product_detail(product_id):
    product = Product.query.get_or_404(product_id)
    return render_template("product.html", product=product)

# Register
@main.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_pw = generate_password_hash(form.password.data)
        new_user = User(username=form.username.data, password=hashed_pw)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("main.login"))
    return render_template("register.html", form=form)

# Login
@main.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for("main.home"))
        else:
            flash("Invalid username or password.")
    return render_template("login.html", form=form)

# Logout
@main.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.login"))

# Add to cart
@main.route("/add-to-cart/<int:product_id>", methods=["POST"])
@login_required
def add_to_cart(product_id):
    user_id = current_user.id
    existing_item = CartItem.query.filter_by(user_id=user_id, product_id=product_id).first()
    if existing_item:
        existing_item.quantity += 1
    else:
        new_item = CartItem(user_id=user_id, product_id=product_id, quantity=1)
        db.session.add(new_item)
    db.session.commit()
    flash("Item added to cart!")
    return redirect(url_for("main.cart"))

# View cart
@main.route("/cart")
@login_required
def cart():
    cart_items = CartItem.query.filter_by(user_id=current_user.id).all()
    return render_template("cart.html", cart_items=cart_items)

# Update cart
@main.route("/update-cart/<int:item_id>", methods=["POST"])
@login_required
def update_cart(item_id):
    action = request.form.get("action")
    item = CartItem.query.get_or_404(item_id)
    if item.user_id != current_user.id:
        flash("Unauthorized action.")
        return redirect(url_for("main.cart"))
    if action == "increase":
        item.quantity += 1
    elif action == "decrease" and item.quantity > 1:
        item.quantity -= 1
    db.session.commit()
    return redirect(url_for("main.cart"))

# Remove from cart
@main.route("/remove-from-cart/<int:item_id>", methods=["POST"])
@login_required
def remove_from_cart(item_id):
    item = CartItem.query.get_or_404(item_id)
    if item.user_id != current_user.id:
        flash("Unauthorized action.")
        return redirect(url_for("main.cart"))
    db.session.delete(item)
    db.session.commit()
    flash("Item removed from cart.")
    return redirect(url_for("main.cart"))

# Category filter
@main.route("/category/<string:category>")
def filter_by_category(category):
    products = Product.query.filter_by(category=category).all()
    return render_template("index.html", products=products, selected_category=category)

# Checkout page
@main.route("/checkout")
@login_required
def checkout():
    cart_items = CartItem.query.filter_by(user_id=current_user.id).all()
    total = sum(item.product.price * item.quantity for item in cart_items)
    return render_template("checkout.html", cart_items=cart_items, total=total)

# Place order (POST)
@main.route("/place_order", methods=["POST"])
@login_required
def place_order():
    name = request.form["name"]
    address = request.form["address"]
    payment_method = request.form["payment_method"]

    cart_items = CartItem.query.filter_by(user_id=current_user.id).all()
    if not cart_items:
        flash("Your cart is empty.")
        return redirect(url_for("main.cart"))

    cart = {
        str(item.product.id): {
            "name": item.product.name,
            "price": item.product.price,
            "quantity": item.quantity
        }
        for item in cart_items
    }

    session["order_data"] = {
        "name": name,
        "address": address,
        "payment_method": payment_method,
        "cart": cart
    }

    return render_template("processing.html")

# Order success
@main.route("/order_success")
@login_required
def order_success():
    order_data = session.pop("order_data", None)
    if not order_data:
        return redirect(url_for("main.home"))

    order_id = f"ORD{random.randint(100000, 999999)}"
    total = sum(item["price"] * item["quantity"] for item in order_data["cart"].values())

    new_order = Order(
        order_id=order_id,
        user_id=current_user.id,  # ✅ This line is essential
        customer_name=order_data["name"],
        address=order_data["address"],
        payment_method=order_data["payment_method"],
        items=json.dumps(order_data["cart"]),
        total=total
    )
    db.session.add(new_order)
    CartItem.query.filter_by(user_id=current_user.id).delete()
    db.session.commit()

    return render_template("order_success.html", order=order_data, order_id=order_id, total=total, timestamp=new_order.timestamp)

# Order History
@main.route("/orders")
@login_required
def order_history():
    orders = Order.query.filter_by(user_id=current_user.id).all()

    # Decode JSON items for each order
    for order in orders:
        order.cart_items = json.loads(order.items)

    return render_template("orders.html", orders=orders)

@main.route("/subscribe", methods=["POST"])
def subscribe():
    email = request.form.get("email")
    if email:
        print(f"📧 New subscriber: {email}")  # You can save this to a database later
        flash("Thanks for subscribing!", "success")
    else:
        flash("Please enter a valid email.", "error")
    return redirect(url_for("main.home"))

@main.route("/privacy")
def privacy():
    return render_template("privacy.html")

@main.route("/terms")
def terms():
    return render_template("terms.html")

@main.route("/help")
def help():
    return render_template("help.html")
