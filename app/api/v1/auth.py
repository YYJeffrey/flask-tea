# -*- coding: utf-8 -*-
"""
    :copyright: (c) 2021 by Jeffrey.
    :license: MIT, see LICENSE for more details.
"""
from app.lib.exception import Success
from app.lib.red_print import RedPrint
from app.service.auth import password_auth
from app.validator.forms import PasswordAuthValidator

api = RedPrint('auth')


@api.route('/login', methods=['POST'])
def login():
    """
    授权登录
    """
    form = PasswordAuthValidator()
    username = form.get_data('username')
    password = form.get_data('password')

    data = password_auth(username, password)
    return Success(data=data)
