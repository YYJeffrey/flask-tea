# -*- coding: utf-8 -*-
"""
    :copyright: (c) 2021 by Jeffrey.
    :license: MIT, see LICENSE for more details.
"""
from dotenv import load_dotenv
from flask import Flask


def create_app():
    load_dotenv(dotenv_path='.flaskenv')
    app = Flask(__name__, static_folder='./static', template_folder='./template')
    return app
