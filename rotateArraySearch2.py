#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random,bisect
from random import randint
from LeetCodeUtils import *
   
def binary_search(a, x, lo=0, hi=None):   # can't use a to specify default for hi
    hi = hi if hi is not None else len(a) # hi defaults to len(a)   
    pos = bisect.bisect_left(a,x,lo,hi)          # find insertion position
    return (pos if pos != hi and a[pos] == x else -1) # don't walk off the end

class Solution:
    # @param A a list of integers
    # @param target an integer
    # @return a boolean
    def search(self, A, target):
        return self.searchPos(A, target) >=0

    def searchPos(self, A, target):
        x = self.search2(A, 0, len(A), target)
        return x

    def search2(self, a, lo, hi, target):
        # print lo, hi
        if lo >= hi:
            return -1
        if a[lo] < a[hi-1]:
            return binary_search(a, target, lo, hi)
        if lo == hi - 1:
            return lo if a[lo] == target else -1
        mid = (lo+hi)/2
        x = self.search2(a, lo, mid, target);
        if x >= 0:
            return x
        return self.search2(a, mid, hi, target)

def searchPos(a, target):
    return Solution().searchPos(a, target)
    pass

def testBasic():
    assert searchPos([1, 2], 1) == 0
    assert searchPos([], 1) == -1
    assert searchPos([-1], 1) == -1
    assert searchPos([1], 1) == 0
    assert searchPos([0], 0) == 0
    assert searchPos([1, 2], 2) == 1
    assert searchPos([1, 2], 3) == -1
    assert searchPos([1, 2, 0], 0) == 2
    assert searchPos([1, 2, -1, 0], -1) == 2

def test2():
    assert searchPos([2,1], 1) == 1
    for i in range(1,100):
        a = [randint(1, 50) for x in range(i)]
        a.sort()
        k = randint(0, len(a)-1)
        rotated = a[k:] + a[:k]

        target = randint(-50, 55)
        expected = binary_search(a, target) >= 0
        assert Solution().search(rotated, target) == expected
    pass