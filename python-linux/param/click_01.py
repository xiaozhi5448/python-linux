#!/usr/bin/env python
import click


@click.command()
@click.option('--host',default='127.0.0.1',type=str, prompt='please input host:',help='the host')
@click.option('--port', default=3306, type=int, prompt="type your port:", help='mysql port')
def connect(host,port):
    print 'connecting ',host,':',port

connect()
