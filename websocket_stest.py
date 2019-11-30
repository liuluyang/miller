# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Miller"
# Datetime: 2019/11/26 16:14

import socket
import base64
import hashlib
from threading import Thread


class WebSocketThread(Thread):
    def __init__(self, conn, *args, **kwargs):
        self.conn = conn
        super().__init__(*args, **kwargs)

    def run(self):
        self.send()

    def send(self):
        data = self.conn.recv(1024)
        print(data)


def create_websocket():
    # 启动Socket 并监听连接
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        sock.bind(("127.0.0.1", 8001))
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.listen(5)
    except Exception as e:
        print(e)
        return

    while True:
        print("websocket start 127.0.0.1:8001......")
        conn, addr = sock.accept()
        data = str(conn.recv(1024))

        header_dict = {}
        header, _ = data.split(r"\r\n\r\n", 1)
        for line in header.split(r"\r\n")[1:]:
            key, val = line.split(":", 1)
            header_dict[key] = val

        if 'Sec-WebSocket-Key' not in header_dict:
            conn.close()
            return
        magic_key = '258EFA5-E914-47DA-95CA-C5AB0DC85B11'
        sec_key = header_dict['Sec-WebSocket-Key'] + magic_key
        key = base64.b64encode(hashlib.sha1(bytes(sec_key, encoding="utf-8")).digest())
        key_str = str(key)[2:30]

        response = '''HTTP/1.1 101 Switching Protocols\r\n
        Connection:Upgrade\r\n
        Upgrade:websocket\r\n
        Sec-WebSocket-Accept:{0}\r\n
        WebSocket-Protocol:char\r\n\r\n'''.format(key_str)
        print(response)
        conn.send(bytes(response, encoding="utf-8"))
        WebSocketThread(conn).start()


create_websocket()
