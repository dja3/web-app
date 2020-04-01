#! /usr/bin/python

import datetime
from bson import ObjectId
from app.services import utils

def getIdea(select=None,
            projection=None):

    try:
        idea = utils.my_idea_find(select=select,
                                  projection=projection)
        idea = [i for i in idea]

        if len(idea) == 0:
            return_code = 404

        else:
            return_code = 200

        body = {
                 "idea" : idea,
                 "idea_count" : len(idea),
                 "timestamp" : str(datetime.datetime.utcnow())
               }

        return body, return_code

    except Exception as e:
        return { "exception_message" : str(e) }, 502

def getIdeaFromID(_id=None,
                  projection=None):

    try:
        idea = utils.my_idea_find_one(select={ "_id" : ObjectId(_id) },
                                      projection=projection)

        if idea == None:
            return_code = 404
            body = {}
        else:
            return_code = 200
            body = {
                     "idea" : idea,
                     "timestamp" : str(datetime.datetime.utcnow())
                   }

        return body, return_code

    except Exception as e:
                 return { "exception_message" : str(e) }, 502

