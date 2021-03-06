# -*- coding: utf-8 -*-
"""
    :copyright: (c) 2021 by Jeffrey.
    :license: MIT, see LICENSE for more details.
"""
import os


class BaseConfig(object):
    """
    基础配置
    """
    # --- 接口相关 ---
    # APP名称 用于请求头校验
    APP_NAME = os.getenv('APP_NAME', 'FLASK-TEA')
    # 不校验请求头的路由 用于放行回调请求
    ALLOWED_PATH = []
    # 是否按REST风格返回状态码
    RESTFUL_HTTP_CODE = False

    # --- 密钥相关 ---
    SECRET_KEY = os.getenv('SECRET_KEY', 'Hello, Flask-Tea!!!')
    EXPIRES_IN = 86400 * 7

    # --- SQLAlchemy相关 ---
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'SQLALCHEMY_DATABASE_URI',
        'mysql+cymysql://root:123456@127.0.0.1:3306/tea?charset=utf8mb4'
    )
    SQLALCHEMY_ENCODING = "utf8mb4"
    # 是否启用追踪对象修改信号
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # 是否启用慢查询记录
    SQLALCHEMY_RECORD_QUERIES = True
    # 连接池选项
    SQLALCHEMY_ENGINE_OPTIONS = {
        'pool_size': 50,
        'max_overflow': 10,
        'pool_recycle': 1800,
        'pool_timeout': 60,
        'pool_pre_ping': True
    }
