from code_delivery.ext.db import db
from code_delivery.ext.site import models

def init_app(app):
    @app.cli.command()
    def create_db():
        """This command initializes the db"""
        db.create_all()
