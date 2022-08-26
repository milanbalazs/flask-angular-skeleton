"""
 The Flask server of Backend.
"""

import logging
import logging.config
import configparser
import os.path

from flask import Flask, jsonify
from flask_restful import Api

from db_handler.mongo_db_handler import DBHandler
from resources.ping import PingResource

# Flask application object
app = Flask(__name__)

# Flask RestFul API object
api = Api(app)

api.add_resource(PingResource, "/ping")


@app.errorhandler(Exception)
def default_error_handler(error):
    """! Default error handler for Server.

    The unhandled error is logged and it will be transferred as standard response
    with 500 status-code which is the Internal Server Error failure.

    Args:
        error (Exception): The Exception that triggered this method.

    Returns:
        Response: The message of exception and 500 status-code Json format (jsonify).
    """

    logging.exception(error)
    return jsonify(message=str(error)), getattr(error, "code", 500)


logging.config.fileConfig(os.path.join(os.path.dirname(__file__), "logging.ini"))

if __name__ == "__main__":

    db_handler = DBHandler()
    db_handler.connect()

    config = configparser.ConfigParser()
    config.read(os.path.join(os.path.dirname(__file__), "config.ini"))

    app.run(
        debug=config.getboolean("BACKEND", "debug_mode"),
        host=config.get("BACKEND", "host"),
        port=config.getint("BACKEND", "port"),
    )
