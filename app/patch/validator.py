# -*- coding: utf-8 -*-
"""
    :copyright: (c) 2021 by Jeffrey.
    :license: MIT, see LICENSE for more details.
"""
from collections import namedtuple

from flask import request
from wtforms import Form as _Form
from wtforms.compat import string_types
from wtforms.validators import StopValidation, DataRequired as _DataRequired

from app.lib.exception import ParameterError


class Form(_Form):
    def __init__(self):
        data = request.get_json(silent=True)
        args = request.args.to_dict()
        super(Form, self).__init__(data=data, **args)

    def validate_for_api(self):
        valid = super(Form, self).validate()
        if not valid:
            msg = ''
            for index, item in enumerate(self.errors.values()):
                msg = msg + ';'.join(item)
                if index != len(self.errors.values()) - 1:
                    msg = msg + ';'
            raise ParameterError(msg=msg)
        return self

    def get_data(self, *args):
        data_list = []
        for arg in args:
            data_list.append(getattr(self._data, arg, None))
        return data_list[0] if len(data_list) == 1 else tuple(data_list)

    @property
    def _data(self):
        self.validate_for_api()
        key_list, value_list = [], []
        for key, value in self._fields.items():
            if value.data is not None:
                key_list.append(key)
                value_list.append(value.data)
        NamedTuple = namedtuple('NamedTuple', [key for key in key_list])
        return NamedTuple(*value_list)

    @property
    def dt_data(self):
        return self._data._asdict()

    @property
    def nt_data(self):
        return self._data


class DataRequired(_DataRequired):
    def __call__(self, form, field):
        if field.type == 'IntegerField' and field.data == 0:
            return

        if not field.data or isinstance(field.data, string_types) and not field.data.strip():
            if self.message is None:
                message = field.gettext('This field is required.')
            else:
                message = self.message

            field.errors[:] = []
            raise StopValidation(message)
