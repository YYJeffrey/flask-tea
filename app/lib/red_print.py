# -*- coding: utf-8 -*-
"""
    :copyright: (c) 2021 by Jeffrey.
    :license: MIT, see LICENSE for more details.
"""


class RedPrint(object):
    def __init__(self, name):
        self.name = name
        self.mound = []

    def route(self, rule, **options):
        def decorator(f):
            self.mound.append((f, rule, options))
            return f

        return decorator

    def register(self, bp, url_prefix=None):
        if url_prefix is None:
            url_prefix = f"/{self.name}"
        for f, rule, options in self.mound:
            endpoint = f"{self.name}+{options.pop('endpoint', f.__name__)}"
            bp.add_url_rule(url_prefix + rule, endpoint, f, **options)
