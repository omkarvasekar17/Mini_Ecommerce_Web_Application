from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime

db = SQLAlchemy()

class User(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column("UserID", db.Integer, primary_key=True)
    username = db.Column("Username", db.String(50), unique=True, nullable=False)
    email = db.Column("Email", db.String(100))
    password_hash = db.Column("PasswordHash", db.String(200), nullable=False)
    role = db.Column("Role", db.String(20), nullable=False, default="Customer")

    products = db.relationship("Product", backref="seller", lazy=True)
    orders = db.relationship("Order", backref="customer", lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Product(db.Model):
    __tablename__ = "products"
    id = db.Column("ProductID", db.Integer, primary_key=True)
    name = db.Column("Name", db.String(100), nullable=False)
    price = db.Column("Price", db.Float, nullable=False)
    stock = db.Column("Stock", db.Integer, nullable=False, default=0)
    description = db.Column("Description", db.String(200), default="")
    seller_id = db.Column(db.Integer, db.ForeignKey("users.UserID"), nullable=False)

    orders = db.relationship("Order", backref="product", lazy=True)


class Order(db.Model):
    __tablename__ = "orders"
    id = db.Column("OrderID", db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.UserID"), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey("products.ProductID"), nullable=False)
    quantity = db.Column("Quantity", db.Integer, nullable=False, default=1)
    order_date = db.Column("OrderDate", db.DateTime, default=datetime.utcnow)
