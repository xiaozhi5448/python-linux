#!/usr/bin/env python
import argparse


def _argparser():
    arg = argparse.ArgumentParser(description="test description")
    arg.add_argument('--host', default="127.0.0.1", help="the host which we will connect", dest="host")
    arg.add_argument('-p', default=3306, type=int, help="the port we connect",dest="port")
    return arg.parse_args()

def main():
    args = _argparser()
    print args
    print args.host
    print args.port


if __name__ == '__main__':
    main()
