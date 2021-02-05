# -*- coding: utf-8 -*-
"""
    :copyright: (c) 2021 by Jeffrey.
    :license: MIT, see LICENSE for more details.
"""
from uuid import uuid4

from sqlalchemy import Column, String, DateTime, func, orm, inspect

from app import db


class BaseModel(db.Model):
    __abstract__ = True

    id = Column('id', String(36), default=lambda: uuid4().hex, primary_key=True, comment='主键标识')
    create_time = Column('create_time', DateTime, server_default=func.now(), comment='创建时间')
    update_time = Column('update_time', DateTime, onupdate=func.now(), comment='更新时间')
    delete_time = Column('delete_time', DateTime, comment='删除时间')

    @orm.reconstructor
    def init_on_load(self):
        """
        初始化
        """
        # 所有字段
        self._fields = []
        # 排除字段
        self._exclude = []

        self.set_fields()
        self.__prune_fields()

    def __prune_fields(self):
        """
        修剪字段
        """
        columns = inspect(self.__class__).columns
        if not self._fields:
            all_columns = set([column.name for column in columns])
            self._fields = list(all_columns - set(self._exclude))

    def set_fields(self):
        """
        设置字段
        """
        pass

    def keys(self):
        return self._fields

    def hide(self, *args):
        for key in args:
            self._fields.remove(key)
        return self

    def __getitem__(self, key):
        return getattr(self, key)

    @property
    def status(self):
        return not self.delete_time

    @classmethod
    def get_one(cls, **kwargs):
        """
        查询一条记录
        """
        return cls.query.filter_by(**kwargs).first()

    @classmethod
    def get_all(cls, **kwargs):
        """
        查询所有记录
        """
        return cls.query.filter_by(**kwargs).all()

    @classmethod
    def create(cls, commit: bool = True, **kwargs):
        """
        新增一条记录
        """
        instance = cls()
        for attr, value in kwargs.items():
            if hasattr(instance, attr):
                setattr(instance, attr, value)
        return instance.save(commit)

    def update(self, commit: bool = True, **kwargs):
        """
        更新一条记录
        """
        for attr, value in kwargs.items():
            if hasattr(self, attr):
                setattr(self, attr, value)
        return self.save(commit)

    def delete(self, commit: bool = True, soft: bool = True):
        """
        删除一条记录 默认软删除
        """
        if soft:
            self.delete_time = func.now()
            self.save()
        else:
            db.session.delete(self)
        commit and db.session.commit()

    def save(self, commit: bool = True):
        """
        保存修改记录
        """
        db.session.add(self)
        if commit:
            db.session.commit()
        return self
