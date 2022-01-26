from flask import Blueprint, render_template, request, flash

from .models import Products
from .products.product import check_stock, create_product
from .web_helper import is_url_valid
from app import db

views = Blueprint("views", __name__)


@views.route("/stock")
def check_stock_page():
    return render_template("stock.html", values=Products.query.all(), check_stock=check_stock)


@ views.route("/products", methods=["POST", "GET"])
def products_page():
    if request.method == "POST":
        if "add-url" in request.form:
            url = request.form["add-url"]
            if is_url_valid(url):
                # if link is not already in the database then add it
                if not Products.query.filter_by(url=url).first():
                    site, name = create_product()
                    db.session.add(Products(url, site, name))
                    db.session.commit()
            else:
                flash("URL not valid.")
        elif "btn-delete" in request.form:
            url = request.form['btn-delete']
            Products.query.filter_by(url=url).delete()
            db.session.commit()

    return render_template("products.html", values=Products.query.all())
