from flask import Flask
from .ext import site
from .ext import config
from .ext import toolbar

def create_app():
    """Factory to create a Flask app based on factory pattern"""
    app = Flask(__name__)
    config.init_app(app)
    toolbar.init_app(app)
    site.init_app(app)
    return app
