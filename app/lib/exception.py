# -*- coding: utf-8 -*-
"""
    :copyright: (c) 2021 by Jeffrey.
    :license: MIT, see LICENSE for more details.
"""
from flask import json, current_app
from werkzeug._compat import text_type
from werkzeug.exceptions import HTTPException


class APIException(HTTPException):
    code = 500
    msg_code = 9999
    data = None
    msg = '服务器未知错误'
    headers = {'Content-Type': 'application/json'}

    def __init__(self, data=None, code=None, msg_code=None, msg=None, headers=None):
        if data:
            self.data = data
        if msg_code:
            self.msg_code = msg_code
        if msg:
            self.msg = msg
        if headers:
            self.headers = headers

        # 状态码返回风格
        if current_app.config['RESTFUL_HTTP_CODE']:
            if code:
                self.code = code
        else:
            self.code = 200

        super(APIException, self).__init__()

    def get_body(self, environ=None):
        body = dict(
            msg_code=self.msg_code,
            msg=self.msg,
            data=self.data
        )
        text = json.dumps(body)
        return text_type(text)

    def get_headers(self, environ=None):
        return [(k, v) for k, v in self.headers.items()]


# --- 成功 0~999 ---
class Success(APIException):
    code = 200
    msg_code = 0
    msg = '成功'


class Created(APIException):
    code = 201
    msg_code = 1
    msg = '创建成功'


class Updated(APIException):
    code = 201
    msg_code = 2
    msg = '更新成功'


class Deleted(APIException):
    code = 201
    msg_code = 3
    msg = '删除成功'


# --- 失败 1000~9999 ---
class Failed(APIException):
    code = 400
    msg_code = 1000
    msg = '失败'


class ParameterError(APIException):
    code = 400
    msg_code = 1001
    msg = '参数错误'


class Duplicated(APIException):
    code = 400
    msg_code = 1002
    msg = '对象已存在'


class NotFound(APIException):
    code = 404
    msg_code = 1003
    msg = '对象未找到'


class ServerError(APIException):
    code = 500
    msg_code = 9999
    msg = '服务器异常'


# --- 权限相关 10000~10099 ---
class UnAuthentication(APIException):
    code = 401
    msg_code = 10000
    msg = '未授权访问'


class PasswordInvalid(APIException):
    code = 401
    msg_code = 10009
    msg = '用户名或密码错误'


class TokenInvalid(APIException):
    code = 401
    msg_code = 10010
    msg = 'Token不合法'


class TokenExpired(APIException):
    code = 401
    msg_code = 10011
    msg = 'Token过期'


class HeaderInvalid(APIException):
    code = 401
    msg_code = 10012
    msg = '请求头不合法'


class Forbidden(APIException):
    code = 403
    msg_code = 10020
    msg = '权限不足'


class MethodNotAllowed(APIException):
    code = 405
    msg_code = 10030
    msg = '方法不被允许'


# --- 文件相关 10100~10199 ---
class FileExtensionError(APIException):
    code = 401
    message = "文件后缀名不合法"
    message_code = 10100


class FileTooLarge(APIException):
    code = 413
    msg_code = 10101
    msg = '文件过大'

# --- 用户业务相关 10200~10299 ---
