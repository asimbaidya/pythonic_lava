from flask import Flask, render_template,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from lava.configs import Config


db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)


    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)


    from lava.main import main
    from lava.posts.routes import posts
    from lava.users.routes import users
    from lava.map import map
    from lava.todo import todo

    app.register_blueprint(main)
    app.register_blueprint(posts)
    app.register_blueprint(users)
    app.register_blueprint(map)
    app.register_blueprint(todo)

    return app
