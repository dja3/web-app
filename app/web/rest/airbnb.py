#! /usr/bin/python

import datetime
import logging

from flask import Blueprint,request,jsonify
from app.web import utils
from app.services.airbnb import get_listings

# logger
log = logging.getLogger()
log.info("new logger")

# create blueprint instance
airbnb_v1_blueprint = Blueprint('airbnb_v1_api', __name__)


@airbnb_v1_blueprint.route('/airbnb/listing', methods=['GET'])
def listings():


    select = {
               "address.country_code" : request.args.get("countryCode"),
               "bedrooms" : int(request.args.get("bedrooms")),
               "property_type" : request.args.get("propertyType")
             }
    # call airbnb service functions
    response = get_listings.getListingID(select=select)

    return response

@airbnb_v1_blueprint.route('/airbnb/listing/<_id>', methods=['GET'])
def get_id(_id):

    response = get_listings.getListingFromID(_id=_id)

    return response
