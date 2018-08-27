#!/usr/bin/env python
import threading
from time import ctime, sleep


secLoop = [6, 4]
def loop(sec, i):
    print 'loop', i, 'start at', ctime()
    sleep(sec)
    print 'loop', i, 'finished at', ctime()


def main():
    nloop = range(len(secLoop))
    threads = []
    for i in nloop:
        threads.append(threading.Thread(target=loop, args=(secLoop[i], i)))

    for i in nloop:
        threads[i].start()

    for i in nloop:
        threads[i].join()

if __name__ == '__main__':
    main()
