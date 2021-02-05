# -*- coding: utf-8 -*-
"""
    :copyright: (c) 2021 by Jeffrey.
    :license: MIT, see LICENSE for more details.
"""
from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate

from app.patch.db import SQLAlchemy, BaseQuery

db = SQLAlchemy(query_class=BaseQuery)
migrate = Migrate(db=db)
cors = CORS(resources={"/*": {"origins": "*"}})


def create_app():
    # 载入环境变量 .env .flaskenv
    load_dotenv()
    app = Flask(__name__, static_folder='./static', template_folder='./template')

    register_config(app)
    register_extension(app)

    return app


def register_config(app):
    """
    注册配置
    """
    flask_env = app.config.get('ENV')
    app.config.from_object(f"app.config.{flask_env}.{flask_env.capitalize()}Config")


def register_extension(app):
    """
    注册拓展
    """
    db.init_app(app)
    migrate.init_app(app)
    cors.init_app(app)
