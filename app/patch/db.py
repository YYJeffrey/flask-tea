# -*- coding: utf-8 -*-
"""
    :copyright: (c) 2021 by Jeffrey.
    :license: MIT, see LICENSE for more details.
"""
from contextlib import contextmanager

from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy, Pagination as _Pagination, BaseQuery as _BaseQuery


class SQLAlchemy(_SQLAlchemy):
    """
    覆写SQLAlchemy
    """

    @contextmanager
    def auto_commit(self):
        """
        自动提交SQL
        """
        try:
            yield
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e


class Pagination(_Pagination):
    """
    覆写Pagination
    """

    def hide(self, *keys):
        """
        隐藏字段
        """
        for item in self.items:
            item.hide(*keys)
        return self

    def append(self, *keys):
        """
        添加字段
        """
        for item in self.items:
            item.append(*keys)
        return self


class BaseQuery(_BaseQuery):
    """
    覆写BaseQuery
    """

    def filter_by(self, soft_del: bool = False, **kwargs):
        """
        默认查询未被软删除的记录
        """
        if soft_del:
            kwargs["delete_time"] = None
        return super(BaseQuery, self).filter_by(**kwargs)

    def paginate(self, page=None, size=None, error_out=True, max_per_page=None):
        """
        覆写分页
        """
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
