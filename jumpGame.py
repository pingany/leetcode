#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob
reload(sys)
sys.setdefaultencoding("utf-8")

MAX_INT = (1 << 30)

def f(a):
    if len(a) < 2:
        return 0
    n = len(a)-1
    ff = [None]*(n+1)
    ff[n] = 0
    x = n -1
    while x >= 0:
        if x + a[x] >= n:
            ff[x] = 1
            x -= 1
            continue
        t = MAX_INT
        step = min(n-x-1, a[x])
        while step >= 1:
            t = min(t, ff[x+step]+1)
            if t <= 2:
                break
            step -= 1
        ff[x] = t
        x -= 1
    return ff[0]

class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        return f(A)

def sp(a, r):
    assert Solution().jump(a) == r

def test():
    sp([2,3,1,1,4], 2)
    sp([], 0)
    sp([1], 0)
    sp([1, 2], 1)
    sp([1, 1, 3], 2)
    sp([2, 1, 3], 1)
    sp([2, 2, 2, 2, 2], 2)
    pass

def test2():
    import json
    Solution().jump(json.load(open('jumpGame.in')))
def main(args):
    
    pass

if __name__ == '__main__':
    main(sys.argv[1:])