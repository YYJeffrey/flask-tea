# -*- coding: utf-8 -*-
"""
    :copyright: (c) 2021 by Jeffrey.
    :license: MIT, see LICENSE for more details.
"""
from uuid import uuid4

from sqlalchemy import Column, String, DateTime, func, orm, inspect

from app.lib.exception import NotFound
from app.patch.db import SQLAlchemy, BaseQuery
from app.validator.forms import PaginateValidator

db = SQLAlchemy(query_class=BaseQuery)


class BaseModel(db.Model):
    """
    基础模型
    """
    __abstract__ = True

    id = Column('id', String(36), default=lambda: uuid4().hex, primary_key=True, comment='主键标识')
    create_time = Column('create_time', DateTime, server_default=func.now(), comment='创建时间', index=True)
    update_time = Column('update_time', DateTime, onupdate=func.now(), comment='更新时间')
    delete_time = Column('delete_time', DateTime, comment='删除时间')

    def __getitem__(self, key):
        return getattr(self, key)

    def __set_fields(self):
        columns = inspect(self.__class__).columns
        all_columns = set([column.name for column in columns])
        self._fields.extend(list(all_columns - set(self._exclude)))

    @orm.reconstructor
    def init_on_load(self):
        """
        无法直接调用构造函数 需使用装饰器
        """
        self._fields = ['status']
        self._exclude = ['delete_time', 'update_time']

        self.__set_fields()

    def keys(self):
        return self._fields

    def hide(self, *keys):
        for key in keys:
            hasattr(self, key) and self._fields.remove(key)
        return self

    def append(self, *keys):
        for key in keys:
            hasattr(self, key) and self._fields.append(key)
        return self

    @property
    def status(self):
        return not self.delete_time

    @classmethod
    def get_or_404(cls, **kwargs):
        rv = cls.query.filter_by(**kwargs).first()
        if not rv:
            raise NotFound
        return rv

    @classmethod
    def all_or_404(cls, **kwargs):
        rv = cls.query.filter_by(**kwargs).all()
        if not rv:
            raise NotFound
        return rv

    @classmethod
    def get_one(cls, **kwargs):
        return cls.query.filter_by(**kwargs).first()

    @classmethod
    def get_all(cls, **kwargs):
        return cls.query.filter_by(**kwargs).all()

    @classmethod
    def create(cls, commit: bool = True, **kwargs):
        instance = cls()
        for attr, value in kwargs.items():
            hasattr(instance, attr) and setattr(instance, attr, value)
        return instance.save(commit)

    def update(self, commit: bool = True, **kwargs):
        for attr, value in kwargs.items():
            hasattr(self, attr) and setattr(self, attr, value)
        return self.save(commit)

    def save(self, commit: bool = True):
        db.session.add(self)
        commit and db.session.commit()
        return self

    def delete(self, commit: bool = True, soft: bool = True):
        """
        删除 默认软删除
        """
        if soft:
            self.delete_time = func.now()
            self.save()
        else:
            db.session.delete(self)
        commit and db.session.commit()

    @classmethod
    def get_pagination(cls, not_del: bool = True):
        """
        分页调用
        """
        validator = PaginateValidator().dt_data
        page = validator.get('page')
        size = validator.get('size')

        paginator = cls.query
        if not_del:
            paginator = paginator.filter_by(delete_time=None)
        return paginator.order_by(cls.create_time.desc()).paginate(page=page, size=size)
