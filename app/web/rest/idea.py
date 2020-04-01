#! /usr/bin/python

import datetime
import logging

from flask import Blueprint,request,jsonify
from app.web import utils
from app.services.idea import create_idea_service, delete_idea_service, update_idea_service, get_idea_service

# create blueprint instance
idea_v1_blueprint = Blueprint('idea_v1_api', __name__)

@idea_v1_blueprint.route('/idea', methods=['GET'])
def idea():

    # Get the list of current ideas
    response = get_idea_service.getIdea()
    logging.debug("response: {}".format(response))

    return response

@idea_v1_blueprint.route('/idea/create', methods=['POST'])
def ideaCreate():

    # get request data
    data = request.get_json()
    logging.debug("request data: {}".format(data))

    # add timestamp to each idea
    for d in data['idea_list']:
        d['origination_timestamp'] = str(datetime.datetime.utcnow())

    # create an idea
    response = create_idea_service.createIdea(data['idea_list'])
    logging.debug("response: {}".format(response))

    return response

@idea_v1_blueprint.route('/idea/<_id>', methods=['GET', 'PUT'])
def ideaId(_id):

    logging.debug("request method: {}".format(request.method))

    if request.method == "GET":
        response = get_idea_service.getIdeaFromID(_id=_id)

    elif request.method == "PUT":
        #TODO
        response = { "message" : "under construction!" }, 200

    logging.debug("response: {}".format(response))

    return response

@idea_v1_blueprint.route('/idea/<idea_uuid>/delete', methods=['DELETE'])
def ideaIdDelete(idea_uuid):

    response = { "message" : "under construction!" }, 200

    logging.debug("response: {}".format(response))

    return response
