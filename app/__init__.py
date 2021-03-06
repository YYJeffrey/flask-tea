# -*- coding: utf-8 -*-
"""
    :copyright: (c) 2021 by Jeffrey.
    :license: MIT, see LICENSE for more details.
"""
import logging
from logging.handlers import RotatingFileHandler

from dotenv import load_dotenv
from flask import Flask, request
from flask_cors import CORS
from flask_migrate import Migrate
from werkzeug.exceptions import HTTPException

from .lib.exception import APIException, ServerError, HeaderInvalid
from .model.base import db
from .model.user import User
from .patch.encoder import JSONEncoder

migrate = Migrate(db=db, render_as_batch=True, compare_type=True, compare_server_default=True)
cors = CORS(resources={'/*': {'origins': '*'}})


def create_app():
    # 载入环境变量 .env .flaskenv
    load_dotenv()
    app = Flask(__name__, static_folder='./static', template_folder='./template')

    register_config(app)
    register_logging(app)
    register_extension(app)
    register_header(app)
    register_exception(app)
    register_encoder(app)
    register_resource(app)

    return app


def register_config(app):
    flask_env = app.config.get('ENV')
    app.config.from_object(f"app.config.{flask_env}.{flask_env.capitalize()}Config")


def register_logging(app):
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(filename)s:%(lineno)d %(message)s')
    handler = RotatingFileHandler('log/app.log', maxBytes=10 * 1024 * 1024, backupCount=100, encoding='UTF-8')
    handler.setFormatter(formatter)
    handler.setLevel(app.config['LOG_LEVEL'])
    app.logger.addHandler(handler)

    @app.before_first_request
    def prod_logging():
        if not app.debug:
            stream_handler = logging.StreamHandler()
            stream_handler.setFormatter(formatter)
            app.logger.addHandler(stream_handler)
            app.logger.setLevel(app.config['LOG_LEVEL'])


def register_extension(app):
    db.init_app(app)
    migrate.init_app(app)
    cors.init_app(app)


def register_header(app):
    @app.before_request
    def header_validator():
        if 'APP_NAME' not in app.config:
            return
        if request.path in app.config['ALLOWED_PATH'] or '*' in app.config['ALLOWED_PATH']:
            return
        if 'X-App-Name' not in request.headers or request.headers['X-App-Name'] != app.config['APP_NAME']:
            raise HeaderInvalid


def register_exception(app):
    @app.errorhandler(Exception)
    def handle_error(e):
        if isinstance(e, APIException):
            return e
        elif isinstance(e, HTTPException):
            return APIException(code=e.code, msg=e.name)
        else:
            if not app.debug:
                return ServerError()
            raise e


def register_encoder(app):
    app.json_encoder = JSONEncoder


def register_resource(app):
    from .api.v1 import create_v1

    app.register_blueprint(create_v1(), url_prefix='/v1')
