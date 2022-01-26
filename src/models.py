from flask_login import UserMixin
from sqlalchemy.sql import func

from app import db


class Users(db.Model, UserMixin):
    __tablename__ = "Users"
    username = db.Column("username", db.String, primary_key=True)
    password = db.Column("password", db.String)
    last_login = db.Column("last_login", db.DateTime(
        timezone=True), default=func.now())

    def __init__(self, username, password):
        self.username = username
        self.password = password


class Products(db.Model):
    __tablename__ = "Products"
    url = db.Column("url", db.String, primary_key=True)
    site_name = db.Column("site_name", db.String)
    product_name = db.Column("product_name", db.String)

    def __init__(self, url, site_name, product_name):
        self.url = url
        self.site_name = site_name
        self.product_name = product_name
        # self.nickname = nickname # currently not implemented
