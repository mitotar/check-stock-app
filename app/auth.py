from flask import Blueprint, render_template, url_for, redirect, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

from .models import Users, Products
from . import db

auth = Blueprint("auth", __name__)


@auth.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "btn-sign-up" in request.form:
            username = request.form["sign-up-user"]
            password1 = request.form["sign-up-pass"]
            password2 = request.form["sign-up-confirm-pass"]

            if Users.query.filter_by(username=username).first():
                flash("Username is not avaible", category="error")
            elif len(username) < 6:
                flash("Username is too short", category="error")
            elif len(password1) < 6:
                flash("Password is too short", category="error")
            elif password1 != password2:
                flash("Passwords do not match", category="error")
            else:
                new_user = Users(username, generate_password_hash(
                    password1, method="sha256"))
                db.session.add(new_user)
                db.session.commit()
                login_user(new_user, remember=True)
                return redirect(url_for("views.check_stock"))
        elif "btn-sign-in" in request.form:
            username = request.form["sign-in-user"]
            password = request.form["sign-in-pass"]
            user = Users.query.filter_by(username=username).first()
            if user:
                if check_password_hash(user.password, password):
                    login_user(user, remember=True)
                    return redirect(url_for("views.check_stock"))
                else:
                    flash("Password is incorrect", category="error")
            else:
                flash("User does not exist", category="error")

    return render_template("index.html")


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.index"))
