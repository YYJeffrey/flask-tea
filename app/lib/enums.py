# -*- coding: utf-8 -*-
"""
    :copyright: (c) 2021 by Jeffrey.
    :license: MIT, see LICENSE for more details.
"""
from enum import Enum as _Enum


class Enum(_Enum):
    @classmethod
    def choices(cls):
        return [(item.name, item.value) for item in cls]


class GenderEnum(Enum):
    UN_KNOW = '未知'
    MAN = '男'
    WOMAN = '女'
