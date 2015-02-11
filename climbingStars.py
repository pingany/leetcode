#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,utils
reload(sys)
sys.setdefaultencoding("utf-8")


class Solution:
    def __init__(self):
        self.caches = []
        pass
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        self.caches = [0]*(n+1)
        self.caches[0] = 1;
        self.caches[1] = 1;
        return self.f(n)

    def f(self, n):
        if self.caches[n]:
            return self.caches[n]
        self.caches[n] = self.f(n-1) + self.f(n-2)
        return self.caches[n]

def test():
    assert Solution().climbStairs(1) == 1
    assert Solution().climbStairs(2) == 2
    assert Solution().climbStairs(3) == 3
    assert Solution().climbStairs(4) == 5
    assert Solution().climbStairs(5) == 8

def main(args):
        
    pass

if __name__ == '__main__':
    main(sys.argv[1:])