from flask import Blueprint, render_template, url_for, redirect, request, flash
from flask_login import login_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash

from models import Users
from app import db

auth = Blueprint("auth", __name__)


@auth.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "sign-up" in request.form:
            username = request.form.get("username")
            password1 = request.form.get("password1")
            password2 = request.form.get("password2")

            if Users.query.filter_by(username=username).first():
                flash("Username is not avaible")
            elif len(username) < 6:
                flash("Username is too shortt")
            elif len(password1) < 6:
                flash("Password is too shortt")
            elif password1 != password2:
                flash("Passwords do not match")
            else:
                new_user = Users(username, generate_password_hash(
                    password1, method="sha256"))

            db.session.commit()
        elif "sign-in" in request.form:
            username = request.form.get("username")
            password = request.form.get("password")

    return render_template("index.html")


@ auth.route("/logout")
def logout():
    return redirect(url_for(auth.index))
