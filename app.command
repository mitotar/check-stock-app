#!/usr/bin/env python3
from flask import Flask, render_template, url_for, redirect, request, session, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.sql import text
import webbrowser

from check_stock import check_stock, Product, validate_url


app = Flask(__name__)  # reference this file
app.secret_key = "\xdb\xf5xn-\xaa\xf4\xdeHw\xacc\xb9\xc8\xcdA\xfe\xcfxT\xe4\xf3\xe4\x89"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///products.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Products(db.Model):
    url = db.Column("url", db.String, primary_key=True)
    product_name = db.Column("product_name", db.String)
    site_name = db.Column("site_name", db.String)

    def __init__(self, product):
        self.url = product.get_url()
        self.product_name = product.get_product_name()
        self.site_name = product.get_site_name()


@app.route("/")
def index():
    return render_template("index.html", values=Products.query.all(), check_stock=check_stock)


@app.route("/products_list", methods=["POST", "GET"])
def products():
    if request.method == "POST":
        if "add_url" in request.form:
            url = request.form["add_url"]
            if validate_url(url):
                if not Products.query.filter_by(url=url).first():
                    product = Product(url)
                    db.session.add(Products(product))
                    db.session.commit()
            else:
                flash("URL not valid.")
        elif "btn_delete" in request.form:
            url = request.form['btn_delete']
            Products.query.filter_by(url=url).delete()
            db.session.commit()

    return render_template("products_list.html", values=Products.query.all())


if __name__ == "__main__":
    webbrowser.open("http://127.0.0.1:5000/")
    db.create_all()
    app.run(debug=False)
