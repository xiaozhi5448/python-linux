#!/usr/bin/env python
from time import ctime
import socket

host='127.0.0.1'
port=8000
addr=(host, port)
bufsize=1024


while True:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(addr)
    data = raw_input(u'>')
    if not data:
        break
    sock.send(data)
    data = sock.recv(bufsize)
    print data

    sock.close()
