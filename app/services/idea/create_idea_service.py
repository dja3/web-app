#! /usr/bin/python

import datetime
from bson import ObjectId
from app.services import utils

def createIdea(idea_list):

    try:
        _id_list = utils.my_idea_insert_many(idea_list)
        logging.debug("_id_list: {}".format( _id_list))

        body = {
                 "create_idea_id_list" : _id_list,
                 "create_idea_count" : len(_id_list),
                 "timestamp" : str(datetime.datetime.utcnow())
               }

        return body, 200

    except Exception as e:
        return { "exception_message" : str(e) }, 502
