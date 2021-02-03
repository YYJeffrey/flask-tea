# -*- coding: utf-8 -*-
"""
    :copyright: (c) 2021 by Jeffrey.
    :license: MIT, see LICENSE for more details.
"""
from .base import BaseConfig


class ProductionConfig(BaseConfig):
    # 关闭SQL语句回显
    SQLALCHEMY_ECHO = False
