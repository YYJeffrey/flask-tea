# -*- coding: utf-8 -*-
"""
    :copyright: (c) 2021 by Jeffrey.
    :license: MIT, see LICENSE for more details.
"""
from app import User
from app.lib.exception import Success, Created, Updated, Deleted, Duplicated
from app.lib.red_print import RedPrint
from app.lib.token import auth
from app.lib.schema import paginator_schema
from app.validator.forms import CreateUserValidator, UpdateUserValidator

api = RedPrint('user')


@api.route('', methods=['GET'])
@auth.login_required
def get_users():
    """
    分页查询用户
    """
    pagination = User.get_pagination().append('update_time', 'delete_time')
    return Success(data=paginator_schema(pagination))


@api.route('/<user_id>', methods=['GET'])
def get_user(user_id):
    """
    查询指定用户
    """
    user = User.get_or_404(id=user_id)
    return Success(data=user)


@api.route('', methods=['POST'])
def create_user():
    """
    创建用户
    """
    form = CreateUserValidator()
    if User.get_one(username=form.get_data('username')):
        raise Duplicated

    User.create(**form.dt_data)
    return Created()


@api.route('/<user_id>', methods=['PUT'])
def update_user(user_id):
    """
    更新指定用户
    """
    form = UpdateUserValidator()
    User.get_or_404(id=user_id).update(**form.dt_data)
    return Updated()


@api.route('/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    """
    删除指定用户
    """
    User.get_or_404(id=user_id).delete()
    return Deleted()
