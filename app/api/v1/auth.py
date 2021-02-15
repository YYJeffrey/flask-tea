# -*- coding: utf-8 -*-
"""
    :copyright: (c) 2021 by Jeffrey.
    :license: MIT, see LICENSE for more details.
"""
from flask import current_app

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
    current_app.logger.info(f'用户: {username}, 登录成功！')

    return Success(data=data)
