"""
MongoDB handler module
"""

import logging
import os
import sys

import pymongo

# Add the backend folder as a Source Root
sys.path.append(os.path.join(os.path.realpath(os.path.dirname(__file__)), ".."))


class DBHandler:
    """
    Class containing methods to communicate with the Database.
    """

    CONNECTION_STRING = "mongodb://root:rootpassword@mongodb:27017/"

    def __init__(self):
        """
        Initializer method used for DBHandler class.
        """

        # Logging object
        self.__logger = logging.getLogger("db_handler")

        self.__logger.info("DBHandler successfully initialized")

        self.__client = None

    def connect(self):
        """
        Method to connect to the MongoDB Database.
        """

        # No need to connect again if there is already a connection.
        if self.__client:
            return

        self.__client = pymongo.MongoClient(DBHandler.CONNECTION_STRING)

        self.__logger.info("Connecting to the Database has been successful")
