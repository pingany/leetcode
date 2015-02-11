#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,utils
import random,bisect

reload(sys)
sys.setdefaultencoding("utf-8")

def binary_search(a, x, lo=0, hi=None):   # can't use a to specify default for hi
    hi = hi if hi is not None else len(a) # hi defaults to len(a)   
    pos = bisect.bisect_left(a,x,lo,hi)          # find insertion position
    return (pos if pos != hi and a[pos] == x else -1) # don't walk off the end

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        x = self.search2(A, 0, len(A), target)
        return x

    def search2(self, a, lo, hi, target):
        print lo, hi
        if lo >= hi:
            return -1
        if a[lo] <= a[hi-1]:
            return binary_search(a, target, lo, hi)
        mid = (lo+hi)/2
        x = self.search2(a, lo, mid, target);
        if x >= 0:
            return x
        return self.search2(a, mid, hi, target)


def testBasic():

    assert Solution().search([1, 2], 1) == 0
    assert Solution().search([], 1) == -1
    assert Solution().search([-1], 1) == -1
    assert Solution().search([1], 1) == 0
    assert Solution().search([0], 0) == 0
    assert Solution().search([1, 2], 2) == 1
    assert Solution().search([1, 2], 3) == -1
    assert Solution().search([1, 2, 0], 0) == 2

def test():
    assert Solution().search([1, 2, -1, 0], -1) == 2

def main(args):
    
    pass

if __name__ == '__main__':
    main(sys.argv[1:])