# -*- coding: utf-8 -*-
"""
    :copyright: (c) 2021 by Jeffrey.
    :license: MIT, see LICENSE for more details.
"""
from app.patch.db import Pagination


def get_paginator_schema(pagination: Pagination = None):
    return {
        'total_size': pagination.total,
        'next_page': pagination.next_num,
        'prev_page': pagination.prev_num,
        'current_page': pagination.page,
        'items': pagination.items
    }
