from flask import Blueprint, redirect, url_for, flash, render_template
from flask_login import login_required, current_user
from models import db, Order, Product

orders_bp = Blueprint("orders", __name__)  # Removed template_folder

@orders_bp.route("/place/<int:product_id>")
@login_required
def place_order(product_id):
    product = Product.query.get_or_404(product_id)
    if product.stock < 1:
        flash("Product out of stock!", "error")
        return redirect(url_for("products.list_products"))

    order = Order(user_id=current_user.id, product_id=product.id, quantity=1)
    product.stock -= 1
    db.session.add(order)
    db.session.commit()
    flash(f"Order placed for {product.name}!", "success")
    return redirect(url_for("orders.view_orders"))

@orders_bp.route("/")
@login_required
def view_orders():
    if current_user.role == "Customer":
        orders = Order.query.filter_by(user_id=current_user.id).all()
    elif current_user.role == "Seller":
        orders = Order.query.join(Product).filter(Product.seller_id == current_user.id).all()
    else:  # Admin
        orders = Order.query.all()

    return render_template("orders/orders.html", orders=orders, user=current_user)
