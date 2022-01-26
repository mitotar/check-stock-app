import webbrowser
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import sys
import logging

from src.views import views
from src.auth import auth
from src.models import Users, Products


ENV = "dev"

app = Flask(__name__)  # reference this file
db = SQLAlchemy(app)

app.secret_key = "\xdb\xf5xn-\xaa\xf4\xdeHw\xacc\xb9\xc8\xcdA\xfe\xcfxT\xe4\xf3\xe4\x89"

if ENV == "prod":
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://ptbmzeoojhjyqn:183d0bd5d83037665ee999566150fb2dc8af79939be350c2db10d6249546af05@ec2-184-73-243-101.compute-1.amazonaws.com:5432/d1sldsv1g5i1pq"
    app.debug = False
elif ENV == "dev":
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///products.sqlite3"
    app.debug = True
    webbrowser.open("http://127.0.0.1:5000/")

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.create_all()

app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)

app.register_blueprint(views, url_prefix="/")
app.register_blueprint(auth, url_prefix="/")

login_manager = LoginManager()
login_manager.login_view = "auth.index"
login_manager.init_app(app)


@login_manager.user_loader
def user_load(username):
    return Users.query.get(username=username)


if __name__ == "__main__":
    app.logger.addHandler(logging.StreamHandler(sys.stdout))
    app.logger.setLevel(logging.ERROR)
    app.run()
