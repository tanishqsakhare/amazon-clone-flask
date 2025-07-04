from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_mail import Mail

db = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate()
mail = Mail()  # ✅ Optional: for sending emails like subscriptions or confirmations

def create_app():
    app = Flask(__name__)

    # 🔐 Configuration
    app.config['SECRET_KEY'] = 'your-secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///store.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # ✉️ Email config (optional, for Flask-Mail)
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USERNAME'] = 'your_email@gmail.com'
    app.config['MAIL_PASSWORD'] = 'your_app_password'  # Use an app password, not your Gmail password

    # 🔧 Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    mail.init_app(app)

    login_manager.login_view = "main.login"

    # 👤 User loader
    from .models import User
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # 📦 Register blueprints
    from .routes import main
    app.register_blueprint(main)

    return app
