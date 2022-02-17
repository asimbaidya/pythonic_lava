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

    @app.route('/')
    def index():
        return render_template('index.html',title='Reports')

    from lava.users.routes import users
    app.register_blueprint(users)
    return app
