from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config
import os

basedir = os.path.abspath(os.path.dirname(__file__))

db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    db.init_app(app)
    db.app = app

    # Register Blueprint
    # main blueprint : api and db operation
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    # spider blueprint : spider script for wanted blog
    from .spider import spider as spider_blueprint
    app.register_blueprint(spider_blueprint)

    with app.app_context():
        db.create_all()

    return app