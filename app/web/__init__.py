#! /usr/bin/python

import decimal
from bson.decimal128 import Decimal128
from bson import ObjectId
from flask import Flask,json

class MyJSONEncoder(json.JSONEncoder):
    """
    Custom JSON encoder to add decimal encoding
    """
    def default(self, obj):
        if isinstance(obj, Decimal128):
            return str(obj)
        elif isinstance(obj, ObjectId):
            return str(obj)
        return super(MyJSONEncoder, self).default(obj)


def create_app():
    web_app = Flask(__name__)
    web_app.json_encoder = MyJSONEncoder

    # create blueprints for api endpoints
    from app.web.rest.status import status_v1_blueprint
    from app.web.rest.session import session_v1_blueprint
    from app.web.rest.airbnb import airbnb_v1_blueprint
    from app.web.rest.idea import idea_v1_blueprint

    # register bluebrints
    web_app.register_blueprint(status_v1_blueprint, url_prefix='/api/v1')
    web_app.register_blueprint(session_v1_blueprint, url_prefix='/api/v1')
    web_app.register_blueprint(airbnb_v1_blueprint, url_prefix='/api/v1')
    web_app.register_blueprint(idea_v1_blueprint, url_prefix='/api/v1')

    return web_app
