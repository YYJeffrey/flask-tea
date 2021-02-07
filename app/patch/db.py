# -*- coding: utf-8 -*-
"""
    :copyright: (c) 2021 by Jeffrey.
    :license: MIT, see LICENSE for more details.
"""
from contextlib import contextmanager

from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy, Pagination as _Pagination, BaseQuery as _BaseQuery


class SQLAlchemy(_SQLAlchemy):
    @contextmanager
    def auto_commit(self):
        try:
            yield
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e


class Pagination(_Pagination):
    def hide(self, *keys):
        for item in self.items:
            item.hide(*keys)
        return self

    def append(self, *keys):
        for item in self.items:
            item.append(*keys)
        return self


class BaseQuery(_BaseQuery):
    def filter_by(self, soft_del: bool = False, **kwargs):
        """
        查询未被软删除的记录
        """
        if not soft_del:
            kwargs['delete_time'] = None
        return super(BaseQuery, self).filter_by(**kwargs)

    def paginate(self, page=None, size=None, error_out=True, max_per_page=None):
        paginator = super(BaseQuery, self).paginate(
            page=page, per_page=size, error_out=error_out, max_per_page=max_per_page
        )
        return Pagination(
            self,
            paginator.page,
            paginator.per_page,
            paginator.total,
            paginator.items
        )
