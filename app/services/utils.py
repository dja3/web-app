#! /usr/bin/python

import logging
from pymongo import MongoClient

# get mongo connection string
with open('mongo/connection', 'r') as f:
    mongo_connection_string=f.read()

try:
    sampleAirbnb = MongoClient(mongo_connection_string)
    idea = MongoClient(mongo_connection_string)

except:
    exit("Can't connect to {}".format(mongo_connection_string))

def my_airbnb_find(select=None,
            projection=None):
    """
    Returns a cursor of all listings in the listingsandReviews collection
    """

    return sampleAirbnb.sample_airbnb.listingsAndReviews.find(select, projection)

def my_airbnb_find_one(select=None,
                       projection=None):

    return sampleAirbnb.sample_airbnb.listingsAndReviews.find_one(select, projection)

def my_idea_find(select=None,
                 projection=None):
    """
    Returns a cursor of all listings in the collection
    """

    return idea.idea.oneBIdeas.find(select, projection)

def my_idea_find_one(select=None,
                     projection=None):
    """
    Returns a single document
    """

    return idea.idea.oneBIdeas.find_one(select, projection)

def my_idea_insert_many(idea_list):

    """
    Inserts n number of ideas into the db and returns the list of _ids
    """

    logging.debug("idea_list: {}".format(idea_list))

    return idea.idea.oneBIdeas.insert_many(idea_list).inserted_ids

def my_idea_delete_many(idea_list):
    """
    Inserts n number of ideas into the db and returns the list of _ids
    """

    return idea.idea.oneBIdeas.delete_many(idea_list)

def my_idea_update_many(idea_list):
    """
    Updatess n number of ideas into the db and returns the list of _ids
    """

    return idea.idea.oneBIdeas.update_many(idea_list).inserted_ids

