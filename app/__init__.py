#! /usr/bin/python

import os
import logging

# TODO maybe move this to the DB later?
token_dict = {}

def run_app():
    from app.web import create_app

    APP_DEBUG = bool(os.environ.get('APP_DEBUG'))

    # start server
    if bool(APP_DEBUG):
        logging.basicConfig(level=logging.DEBUG)
        logging.info("Log level set to: DEBUG")
        create_app().run(host='0.0.0.0', debug=True, port=80)
    else:
        logging.basicConfig(level=logging.INFO)
        logging.info("Log level set to: INFO")
        create_app().run(host='0.0.0.0', debug=False, port=80)

if __name__ == "__main__":
    run_app()
