# -*- coding: utf-8 -*-
"""
    :copyright: (c) 2021 by Jeffrey.
    :license: MIT, see LICENSE for more details.
"""
from dotenv import load_dotenv
from flask import Flask


def create_app():
    # 载入.env和.flaskenv环境变量
    load_dotenv()
    app = Flask(__name__, static_folder='./static', template_folder='./template')
    register_config(app)
    return app


def register_config(app):
    """
    根据FLASK_ENV加载配置
    """
    flask_env = app.config.get('ENV')
    app.config.from_object(f"app.config.{flask_env}.{flask_env.capitalize()}Config")
