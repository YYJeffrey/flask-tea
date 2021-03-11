# -*- coding: utf-8 -*-
"""
    :copyright: (c) 2021 by Jeffrey.
    :license: MIT, see LICENSE for more details.
"""
from sqlalchemy import Column, String, Integer, Enum
from werkzeug.security import generate_password_hash

from app.lib.enums import GenderEnum
from app.model.base import BaseModel


class User(BaseModel):
    """
    用户模型
    """
    __tablename__ = 'user'

    username = Column(String(32), unique=True, nullable=False, comment='用户名', index=True)
    _password = Column('password', String(128), nullable=False, comment='密码')
    nickname = Column(String(32), comment='昵称')
    mobile = Column(String(16), comment='手机号')
    avatar = Column(String(256), comment='头像')
    age = Column(Integer, comment='年龄')
    gender = Column(Enum(GenderEnum), default=GenderEnum.UN_KNOW, comment='性别')

    def __str__(self):
        return self.username

    def keys(self):
        self.hide('password').append('name')
        return self._fields

    @property
    def name(self):
        return self.nickname if self.nickname else self.username

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = generate_password_hash(value)
