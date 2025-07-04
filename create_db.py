from app import create_app, db
app = create_app()
app.app_context().push()
db.create_all()  # This creates all tables defined in models.py
exit()

from app import create_app, db
from app.models import Product

from app.models import User, Product, Order, CartItem  

app = create_app()

with app.app_context():
    db.create_all()
    print("✅ Database tables created.")


app = create_app()
app.app_context().push()

p1 = Product(name="Wireless Mouse", price=499.00, description="Ergonomic wireless mouse", image="mouse.jpg")
p2 = Product(name="Bluetooth Speaker", price=1299.00, description="Portable speaker with deep bass", image="speaker.jpg")

db.session.add_all([p1, p2])
db.session.commit()
print("Sample products added successfully!")

from app import create_app, db
app = create_app()
app.app_context().push()
db.create_all()

from app import create_app, db
from app.models import Product

app = create_app()

with app.app_context():
    # Clear existing products (optional)
    Product.query.delete()

    # Sample products
    products = [
        Product(name="iPhone 14", price=79999, image="iphone.jpg", category="Mobiles"),
        Product(name="Samsung Galaxy S23", price=69999, image="samsung.jpg", category="Mobiles"),
        Product(name="Men's T-Shirt", price=799, image="tshirt.jpg", category="Fashion"),
        Product(name="Women's Jeans", price=1299, image="jeans.jpg", category="Fashion"),
        Product(name="Bluetooth Speaker", price=2499, image="speaker.jpg", category="Electronics"),
        Product(name="Smart LED TV", price=29999, image="tv.jpg", category="Electronics"),
        Product(name="Sofa Set", price=19999, image="sofa.jpg", category="Home"),
        Product(name="Wall Clock", price=499, image="clock.jpg", category="Home"),
        Product(name="Microwave Oven", price=8999, image="microwave.jpg", category="Appliances"),
        Product(name="Washing Machine", price=15999, image="washing.jpg", category="Appliances"),
        Product(name="Atomic Habits", price=499, image="atomic.jpg", category="Books"),
        Product(name="The Alchemist", price=399, image="alchemist.jpg", category="Books"),
        Product(name="Echo Dot (Deal)", price=2999, image="echo_dot.jpg", category="Deals"),
        Product(name="Fitness Band (Deal)", price=1499, image="band.jpg", category="Deals"),
        
        #laptops
        Product(name="MacBook Air M2", price=114999, image="macbook.jpg", category="Laptops"),
        Product(name="Dell XPS 13", price=99999, image="dellxps.jpg", category="Laptops"),
        Product(name="HP Pavilion 15", price=64999, image="hp.jpg", category="Laptops"),
        Product(name="Lenovo IdeaPad Slim 5", price=52999, image="lenovo.jpg", category="Laptops"),
        Product(name="ASUS Vivobook", price=47999, image="asus.jpg", category="Laptops"),
        Product(name="Acer Aspire 7", price=55999, image="acer.jpg", category="Laptops"),

        # Gaming
        Product(name="PS5 Console", price=49999, image="ps5.jpg", category="Gaming"),
        Product(name="Xbox Wireless Controller", price=5999, image="xbox.jpg", category="Gaming"),
        Product(name="Logitech Gaming Mouse", price=1499, image="gamingmouse.jpg", category="Gaming"),
        Product(name="Razer Mechanical Keyboard", price=3499, image="keyboard.jpg", category="Gaming"),
        Product(name="Gaming Headset", price=2999, image="headset.jpg", category="Gaming"),
        Product(name="Nintendo Switch", price=32999, image="switch.jpg", category="Gaming"),

        # Kitchen
        Product(name="Air Fryer", price=6499, image="airfryer.jpg", category="Kitchen"),
        Product(name="Knife Set", price=999, image="knives.jpg", category="Kitchen"),
        Product(name="Mixer Grinder", price=3499, image="mixer.jpg", category="Kitchen"),
        Product(name="Toaster", price=1299, image="toaster.jpg", category="Kitchen"),
        Product(name="Electric Kettle", price=1199, image="kettle.jpg", category="Kitchen"),
        Product(name="Non-Stick Pan", price=799, image="pan.jpg", category="Kitchen"),

        # Fitness
        Product(name="Yoga Mat", price=999, image="yogamat.jpg", category="Fitness"),
        Product(name="Dumbbells Set", price=1999, image="dumbbells.jpg", category="Fitness"),
        Product(name="Resistance Band", price=499, image="resistanceband.jpg", category="Fitness"),
        Product(name="Treadmill", price=34999, image="treadmill.jpg", category="Fitness"),
        Product(name="Skipping Rope", price=299, image="rope.jpg", category="Fitness"),
        Product(name="Foam Roller", price=899, image="roller.jpg", category="Fitness"),

        # Stationery
        Product(name="Notebook Pack", price=299, image="notebooks.jpg", category="Stationery"),
        Product(name="Gel Pens Set", price=199, image="pens.jpg", category="Stationery"),
        Product(name="Sketchbook", price=399, image="sketchbook.jpg", category="Stationery"),
        Product(name="Highlighters", price=149, image="highlighters.jpg", category="Stationery"),
        Product(name="Sticky Notes", price=99, image="stickynotes.jpg", category="Stationery"),
        Product(name="Art Supplies Kit", price=799, image="artkit.jpg", category="Stationery"),
    ]

    db.session.add_all(products)
    db.session.commit()
    print("✅ Sample products added successfully.")
