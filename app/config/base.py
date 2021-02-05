# -*- coding: utf-8 -*-
"""
    :copyright: (c) 2021 by Jeffrey.
    :license: MIT, see LICENSE for more details.
"""
import os


class BaseConfig(object):
    APP_NAME = os.getenv('APP_NAME', 'FLASK-TEA')
    # --- 密钥配置 ---
    SECRET_KEY = os.getenv('SECRET_KEY', 'Hello, Flask-Tea!!!')
    EXPIRES_IN = 86400 * 30

    # --- SQLAlchemy配置 ---
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'SQLALCHEMY_DATABASE_URI',
        'mysql+cymysql://root:123456@127.0.0.1:3306/tea?charset=utf8mb4'
    )
    SQLALCHEMY_ENCODING = "utf8mb4"
    # 关闭追踪对象修改信号
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # 启用慢查询记录
    SQLALCHEMY_RECORD_QUERIES = True
    # 连接池选项
    SQLALCHEMY_ENGINE_OPTIONS = {
        'pool_size': 50,
        'max_overflow': 10,
        'pool_recycle': 1800,
        'pool_timeout': 60,
        'pool_pre_ping': True
    }
