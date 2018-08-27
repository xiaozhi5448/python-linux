
#!/usr/bin/env python
import threading
from time import ctime, sleep


secLoop = [6, 4]
def loop(sec, i):
    print 'loop', i, 'start at', ctime()
    sleep(sec)
    print 'loop', i, 'finished at', ctime()

class ThreadFunc(object):
    def __init__(self, func, args):
        self.func = func
        self.args = args

    def __call__(self):
        apply(self.func,self.args)

def main():
    nloop = range(len(secLoop))
    threads = []
    for i in nloop:
        threads.append(threading.Thread(target=ThreadFunc(loop,(secLoop[i],i))))

    for i in nloop:
        threads[i].start()

    for i in nloop:
        threads[i].join()

if __name__ == '__main__':
    main()
