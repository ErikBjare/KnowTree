import os
import logging

from flask import Flask


def create_app(flask_config_name=None, **kwargs):
    """
    Entry point to the Flask RESTful Server application.
    """
    app = Flask(__name__, **kwargs)

    if app.debug:
        logging.getLogger('flask_oauthlib').setLevel(logging.DEBUG)
        app.logger.setLevel(logging.DEBUG)

    from . import extensions
    extensions.init_app(app)

    from . import modules
    modules.init_app(app)

    return app
