# -*- coding: utf-8 -*-
"""
    :copyright: (c) 2021 by Jeffrey.
    :license: MIT, see LICENSE for more details.
"""
from wtforms import StringField, IntegerField
from wtforms.validators import length, Regexp, NumberRange

from app.lib.enums import GenderEnum
from app.patch.validator import Form, DataRequired, Optional, SelectField


class UpdateUserValidator(Form):
    username = StringField('用户名', validators=[DataRequired(message='用户名不能为空')])
    password = StringField('密码', validators=[DataRequired(message='密码不能为空')])
    nickname = StringField('昵称')
    avatar = StringField('头像')
    gender = SelectField('性别', choices=GenderEnum.choices(), validators=[Optional()])
    age = IntegerField('年龄', validators=[Optional(), NumberRange(min=1, max=500, message='年龄超出可选范围')])
    mobile = StringField('手机', validators=[
        Optional(),
        length(min=11, max=11, message='手机号长度为11位'),
        Regexp(r'^1[3-9]\d{9}$', message='手机号不合法'),
    ])
