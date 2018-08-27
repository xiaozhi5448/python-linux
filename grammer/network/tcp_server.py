#!/usr/bin/env python
import socket
from time import ctime


host='127.0.0.1'
port=8000
bufsize=1024
addr=(host, port)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(addr)
sock.listen(5)
while True:
    print 'waiting for connection...'
    clisock, cliaddr = sock.accept()
    print 'connected from', cliaddr
    print 'peername:', clisock.getpeername()
    data = clisock.recv(bufsize)
    if not data:
        break
    clisock.send('[%s] %s' % (ctime(), data))
    clisock.close()
sock.close()
