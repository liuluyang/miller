# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/11/5 16:07


from wsgiref.simple_server import make_server


def application(environ, start_response):
    print(environ)
    start_response("200 OK", [("Content-Type", "text/html")])
    return [b"<h1>hello world!<h1>"]


httpd = make_server("127.0.0.1", 8000, application)
httpd.serve_forever()



