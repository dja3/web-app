#! /usr/bin/python

import datetime
import logging
import uuid
from flask import Blueprint
from app.web import utils

#from app import session_dict

# logger
log = logging.getLogger()
log.info("new logger")

# create blueprint instance
session_v1_blueprint = Blueprint('session_v1_api', __name__)

@session_v1_blueprint.route('/session/', methods=['POST'])
def create_session():

    session_uuid = str(uuid.uuid1())
    session_timestamp = str(datetime.datetime.utcnow())

    body = {
             "session_uuid" : session_uuid,
             "timestamp" : session_timestamp
           }

    return body, 200
