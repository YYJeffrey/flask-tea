# -*- coding: utf-8 -*-
"""
    :copyright: (c) 2021 by Jeffrey.
    :license: MIT, see LICENSE for more details.
"""
import logging

from .base import BaseConfig


class ProductionConfig(BaseConfig):
    """
    生成环境配置
    """
    LOG_LEVEL = logging.INFO
    # 是否启用SQL语句回显
    SQLALCHEMY_ECHO = False
