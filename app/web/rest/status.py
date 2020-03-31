#! /usr/bin/python

import datetime
import logging
from flask import Blueprint

# logger
log = logging.getLogger()
log.info("new logger")

# create blueprint instance

status_v1_blueprint = Blueprint('status_v1_api', __name__)

@status_v1_blueprint.route('/status/', methods=['GET'])
def status():

    body = {
             "message" : "alive!",
             "timestamp" : str(datetime.datetime.utcnow())
           }

    return body, 200
