mZ!/usr/bin/env python
# coding=utf-8
from operator import add,sub
from random import choice,randint

ops={'+':add,'-':sub}
MAX_TRIES=2

def doprop():
    op=choice('+-')
    nums=[randint(1,10) for i in range(2)]
    nums.sort(reverse=True)
    ans=ops[op](*nums)
    pr='%d %s %d = ' % (nums[0],op,nums[1])
    oops=0
    while True:
        if int(raw_input(pr)==ans:
            print correct
            break

        if oops==MAX_TRIES:
               print 'ans=%d'%(ans)
        else:
               print 'incorrect try again!'
               oops+=1


