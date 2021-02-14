# -*- coding: utf-8 -*-
"""
    :copyright: (c) 2021 by Jeffrey.
    :license: MIT, see LICENSE for more details.
"""
from flask import Blueprint
from . import user
from . import auth


def create_v1():
    bp = Blueprint('v1', __name__)

    user.api.register(bp)
    auth.api.register(bp)

    return bp
