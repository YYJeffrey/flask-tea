# -*- coding: utf-8 -*-
"""
    :copyright: (c) 2021 by Jeffrey.
    :license: MIT, see LICENSE for more details.
"""
from werkzeug.security import check_password_hash

from app import User
from app.lib.exception import NotFound, PasswordInvalid
from app.lib.token import generate_token


def password_auth(username, password):
    user = User.get_one(username=username)
    if not user:
        raise NotFound

    if check_password_hash(user.password, password):
        return {
            'user_id': user.id,
            'username': user.username,
            'token': generate_token(user.id)
        }

    raise PasswordInvalid
