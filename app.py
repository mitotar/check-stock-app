import webbrowser
from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
import sys
import logging

from src.product import check_stock, create_product
from src.web_helper import is_url_valid


ENV = "prod"

app = Flask(__name__)  # reference this file
db = SQLAlchemy(app)

app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)


class Products(db.Model):
    __tablename__ = "Products"
    url = db.Column("url", db.String, primary_key=True)
    site_name = db.Column("site_name", db.String)
    product_name = db.Column("product_name", db.String)

    def __init__(self, url):
        product = create_product(url)
        self.url = url
        self.site_name = product[0]
        self.product_name = product[1]
        # self.nickname = nickname # currently not implemented


@app.route("/")
def index():
    return render_template("index.html", values=Products.query.all(), check_stock=check_stock)


@ app.route("/products_list", methods=["POST", "GET"])
def products():
    if request.method == "POST":
        if "add_url" in request.form:
            url = request.form["add_url"]
            if is_url_valid(url):
                # if link is not already in the database then add it
                if not Products.query.filter_by(url=url).first():
                    db.session.add(Products(url))
                    db.session.commit()
            else:
                flash("URL not valid.")
        elif "btn_delete" in request.form:
            url = request.form['btn_delete']
            Products.query.filter_by(url=url).delete()
            db.session.commit()

    return render_template("products_list.html", values=Products.query.all())


if __name__ == "__main__":
    app.secret_key = "\xdb\xf5xn-\xaa\xf4\xdeHw\xacc\xb9\xc8\xcdA\xfe\xcfxT\xe4\xf3\xe4\x89"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    if ENV == "prod":
        app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://ptbmzeoojhjyqn:183d0bd5d83037665ee999566150fb2dc8af79939be350c2db10d6249546af05@ec2-184-73-243-101.compute-1.amazonaws.com:5432/d1sldsv1g5i1pq"
        app.debug = False
    elif ENV == "dev":
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///products.sqlite3"
        app.debug = True
        webbrowser.open("http://127.0.0.1:5000/")

    db.create_all()
    app.run()
