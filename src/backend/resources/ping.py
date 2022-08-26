"""
Ping RestFul API end-point module
"""

import logging
import os
import sys

from flask import Response, request, jsonify
from flask_restful import Resource

sys.path.append(os.path.dirname(__file__))

from http_status_codes import HttpStatusCodes  # noqa: E402


class PingResource(Resource):
    """
    Ping RestFul API end-point implementations.
    """

    def __init__(self):
        """
        Init method of "PingResource" class.
        """

        super().__init__()

        # Logging object
        self.__logger = logging.getLogger("ping_resource")

    def get(self) -> Response:
        """
        GET method implementations.
        """

        getting_data = self.__load_data_from_request()

        if getting_data:
            self.__logger.info(f"Given data (Do nothing with them): {getting_data}")

        response = jsonify({"message": "Server is up and running"})
        response.status_code = HttpStatusCodes.OK

        return response

    def post(self) -> Response:
        """
        POST method implementations.
        """

        return self.get()

    def __load_data_from_request(self):
        """
        Get data from request.
        """

        try:
            getting_data = request.get_json(force=True)
            self.__logger.info(f"The getting data structure:\n{getting_data}")
        except Exception:
            return None

        return getting_data
