#!/usr/bin/env python
# encoding:utf-8
def Consumer():
    r = ''
    while True:
        res = yield r
        if not res:
            return
        print('[Consumer] consuming {}...'.format(res))
        r = '200 OK'


def Producer(con):
    n = 0
    con.send(None)
    while n < 6:
        n = n+1
        print('[Producer] produceing {}'.format(n))
        res = con.send(n)
        print('[Producer] Consumer return {}'.format(res))

c = Consumer()
Producer(c)

