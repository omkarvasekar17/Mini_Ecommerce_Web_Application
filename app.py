import os
from flask import Flask, redirect, url_for, render_template
from flask_login import LoginManager, current_user
from models import db, User

app = Flask(__name__)
app.secret_key = "secret_key_for_session"

# ================= DATABASE CONFIG =================
db_path = os.path.abspath("ecommerce.db")
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_path}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Initialize DB
db.init_app(app)

# ================= FLASK-LOGIN =================
login_manager = LoginManager()
login_manager.login_view = "users.login"
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# ================= HOMEPAGE =================
@app.route("/")
def home():
    if current_user.is_authenticated:
        return redirect(url_for("products.list_products"))
    return render_template("home.html")  # uses your home.html template

# ================= CREATE TABLES & DEFAULT ADMIN =================
with app.app_context():
    db.create_all()  # Creates tables if they don't exist
    if not User.query.filter_by(username="admin").first():
        admin = User(username="admin", email="admin@example.com", role="Admin")
        admin.set_password("admin123")
        db.session.add(admin)
        db.session.commit()
        print("✅ Default admin created: admin / admin123")

# ================= REGISTER BLUEPRINTS =================
from routes.users.users import users_bp
from routes.products.products import products_bp
from routes.orders.orders import orders_bp

app.register_blueprint(users_bp, url_prefix="/users")
app.register_blueprint(products_bp, url_prefix="/products")
app.register_blueprint(orders_bp, url_prefix="/orders")

# ================= RUN APP =================
if __name__ == "__main__":
    app.run(debug=True)
