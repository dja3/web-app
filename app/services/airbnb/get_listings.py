#! /usr/bin/python

import datetime
from app.services import utils

def getListingID(select=None,
                 projection={ "_id" : 1 } ):

    try:
        listing = utils.my_airbnb_find(select=select,
                                projection=projection)
        listing = [l['_id'] for l in listing]

        body = {
                 "listing" : listing,
                 "listing_count" : len(listing),
                 "timestamp" : str(datetime.datetime.utcnow())
               }

        return body, 200

    except Exception as e:
        return { "exception_message" : str(e) }, 502

def getListingFromID(_id=None,
                     projection=None):

    try:
        listing = utils.my_airbnb_find_one(select={ "_id" : _id },
                                    projection=projection)

        body = {
                 "listing" : listing,
                 "timestamp" : str(datetime.datetime.utcnow())
               }

        return body, 200

    except Exception as e:
                 return { "exception_message" : str(e) }, 502

