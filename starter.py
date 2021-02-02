# -*- coding: utf-8 -*-
"""
    :copyright: (c) 2021 by Jeffrey.
    :license: MIT, see LICENSE for more details.
"""
from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run()
