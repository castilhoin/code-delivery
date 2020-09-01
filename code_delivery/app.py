from flask import Flask

def create_app():
    """Factory to create a Flask app based on factory pattern"""
    app = Flask(__name__)
    return app
