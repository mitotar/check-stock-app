from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user

from .models import Users, Products
from .products.product import check_stock as checkstock, create_product
from .web_helper import is_url_valid
from . import db

views = Blueprint("views", __name__)


@views.route("/stock")
@login_required
def check_stock():
    return render_template("stock.html", values=Products.query.filter_by(username=current_user.username).all(), check_stock=checkstock)


@views.route("/products", methods=["POST", "GET"])
@login_required
def products():
    if request.method == "POST":
        if "add-url" in request.form:
            url = request.form["add-url"]
            if is_url_valid(url):
                # if link is not already in the database then add it
                if not Products.query.filter_by(url=url, username=current_user.username).first():
                    site, name = create_product(url)
                    db.session.add(
                        Products(url, site, name, current_user.username))
                    db.session.commit()
            else:
                flash("URL not valid.")
        elif "btn-delete" in request.form:
            url = request.form['btn-delete']
            Products.query.filter_by(
                url=url, user=current_user.username).delete()
            db.session.commit()

    return render_template("products.html", values=Products.query.filter_by(username=current_user.username).all())
