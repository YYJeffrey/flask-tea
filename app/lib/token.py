# -*- coding: utf-8 -*-
"""
    :copyright: (c) 2021 by Jeffrey.
    :license: MIT, see LICENSE for more details.
"""
from flask import current_app, g
from flask_httpauth import HTTPTokenAuth
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired

from app.lib.exception import TokenInvalid, TokenExpired

auth = HTTPTokenAuth(scheme='Token')


@auth.verify_token
def verify_token(token):
    s = Serializer(
        secret_key=current_app.config['SECRET_KEY'],
        expires_in=current_app.config['EXPIRES_IN']
    )
    try:
        data = s.loads(token)
    except BadSignature:
        raise TokenInvalid
    except SignatureExpired:
        raise TokenExpired
    g.user_id = data['user_id']
    return True


def generate_token(user_id):
    s = Serializer(
        secret_key=current_app.config['SECRET_KEY'],
        expires_in=current_app.config['EXPIRES_IN']
    )
    token = s.dumps({
        'user_id': user_id,
    })
    return token.decode('ascii')
