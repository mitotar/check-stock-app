import webbrowser
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


db = SQLAlchemy()


def create_app(env):
    app = Flask(__name__)  # reference this file

    app.secret_key = "\xdb\xf5xn-\xaa\xf4\xdeHw\xacc\xb9\xc8\xcdA\xfe\xcfxT\xe4\xf3\xe4\x89"

    if env == "prod":
        app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://ptbmzeoojhjyqn:183d0bd5d83037665ee999566150fb2dc8af79939be350c2db10d6249546af05@ec2-184-73-243-101.compute-1.amazonaws.com:5432/d1sldsv1g5i1pq"
        app.debug = False
    elif env == "dev":
        app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///products.sqlite3"
        app.debug = True
        webbrowser.open("http://127.0.0.1:5000/")

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    from .auth import auth
    from .views import views

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    # from .models import Users, Products
    import app.models as models

    db.create_all(app=app)

    login_manager = LoginManager()
    login_manager.login_view = "auth.index"
    login_manager.init_app(app)

    @login_manager.user_loader
    def user_load(id):
        return models.Users.query.get(int(id))

    return app
