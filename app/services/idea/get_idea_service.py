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

        body = {
                 "idea" : idea,
                 "idea_count" : len(idea),
                 "timestamp" : str(datetime.datetime.utcnow())
               }

        return body, 200

    except Exception as e:
        return { "exception_message" : str(e) }, 502

def getIdeaFromID(_id=None,
                  projection=None):

    try:
        idea = utils.my_idea_find_one(select={ "_id" : ObjectId(_id) },
                                      projection=projection)

        body = {
                 "idea" : idea,
                 "timestamp" : str(datetime.datetime.utcnow())
               }

        return body, 200

    except Exception as e:
                 return { "exception_message" : str(e) }, 502

