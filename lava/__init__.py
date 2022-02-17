from flask import Flask, render_template,url_for
from lava.configs import Config

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)



    @app.route('/')
    def index():
        return render_template('index.html',title='Reports')

    from lava.users.routes import users
    app.register_blueprint(users)
    return app
