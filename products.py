from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from models import db, Product

products_bp = Blueprint("products", __name__)  # Removed template_folder

@products_bp.route("/")
@login_required
def list_products():
    products = Product.query.all()
    return render_template("products/products.html", products=products, user=current_user)

@products_bp.route("/add", methods=["GET", "POST"])
@login_required
def add_product():
    if current_user.role != "Seller":
        flash("Only sellers can add products!", "error")
        return redirect(url_for("products.list_products"))

    if request.method == "POST":
        name = request.form.get("name")
        price = float(request.form.get("price"))
        stock = int(request.form.get("stock"))
        description = request.form.get("description")

        product = Product(name=name, price=price, stock=stock, description=description, seller_id=current_user.id)
        db.session.add(product)
        db.session.commit()
        flash("Product added!", "success")
        return redirect(url_for("products.list_products"))

    return render_template("products/add_product.html")
