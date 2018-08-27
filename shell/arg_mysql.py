from __future__ import print_function
import argparse


def _getargs():
    parser = argparse.ArgumentParser(description='test mysql command')
    parser.add_argument('--host', '-H', action='store', type=str, default='127.0.0.1', dest='server')
    parser.add_argument('--port', '-P', action='store', type=int, default=3306, dest='port')
    parser.add_argument('--password', '-p', action='store', required=True, type=str, default='', dest='password')
    parser.add_argument('--version', '-v', action='version', version='%(prog)s 0.1')
    parser.add_argument('--user', '-u', action='store', type=str, required=True, dest='user', help='the user used to connect to the server')
    return parser.parse_args()

args = _getargs()
print (args)

