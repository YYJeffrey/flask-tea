# -*- coding: utf-8 -*-
"""
    :copyright: (c) 2021 by Jeffrey.
    :license: MIT, see LICENSE for more details.
"""
import logging

from .base import BaseConfig


class DevelopmentConfig(BaseConfig):
    LOG_LEVEL = logging.DEBUG
    # 是否启用SQL语句回显
    SQLALCHEMY_ECHO = True
