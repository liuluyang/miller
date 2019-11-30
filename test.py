# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/11/26 9:01

from wsgiref.simple_server import make_server
from urllib.parse import urlunparse


def application(environ, start_response):
    data = environ.get("wsgi.input").read1()
    print(data)
    start_response("200  ", [("Content-Type", "text/html")])
    return [b"OKOKOKOKOKOK"]


http_d = make_server("192.168.1.1", 8800, application)
http_d.serve_forever()
