from __future__ import print_function
import argparse


def _argparse():
    parser = argparse.ArgumentParser(description='this is description')
    parser.add_argument('--host', '-H', action='store', type=str, default='127.0.0.1', dest='host', help='connect to host')
    parser.add_argument('--port', '-p', action='store', type=int, default=80, dest='port', help='dest port')
    return parser.parse_args()

args = _argparse()
print(args)
print(args.host)
print(args.port)
