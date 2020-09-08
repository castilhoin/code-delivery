from flask import Flask
from .ext import site
from .ext import config
from .ext import toolbar
from .ext import db
from .ext import migrate
from .ext import cli

def create_app():
    """Factory to create a Flask app based on factory pattern"""
    app = Flask(__name__)
    config.init_app(app)
    db.init_app(app)
    migrate.init_app(app)
    cli.init_app(app)
    toolbar.init_app(app)
    site.init_app(app)
    return app
