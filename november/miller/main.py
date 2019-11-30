# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/11/6 10:17


from wsgiref.simple_server import make_server


# def application(environ, start_response):
#     start_response("200 OK", [("Content-Type", "text/html")])
#     return [b"<h1>hello world!<h1>"]


def application(environ, start_response):
    start_response("200 OK", [("Content-Type", "text/html")])
    path = environ.get("PATH_INFO")
    if path == "/login":
        with open("./login.html", "rb") as f:
            data = f.read()
        return [data]
    elif path == "/index":
        with open("./index.html", "rb") as f:
            data = f.read()
        return [data]

    return [b"<h1>hello world!<h1>"]


httpd = make_server("", 8000, application)

httpd.serve_forever()




