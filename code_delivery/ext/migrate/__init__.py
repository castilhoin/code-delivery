from flask_migrate import Migrate
from code_delivery.ext.db import db
from code_delivery.ext.db import models

migrate = Migrate()

def init_app(app):
    migrate.init_app(app, db)
