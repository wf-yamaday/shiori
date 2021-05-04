from flask import Flask
from infrastructure.database import db
from flask_marshmallow import Marshmallow

import config


def create_app():
    app = Flask(__name__)
    ma = Marshmallow(app)
    app.config.from_object('config.Config')

    return app


app = create_app()
