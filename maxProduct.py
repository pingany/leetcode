#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random
from random import randint
from LeetCodeUtils import *

def mul(list):
    return reduce(lambda x,y:x*y, list, 1)
def mulSubList(list, startIndex,endIndex):
    return reduce(lambda x,y:x*list[y], xrange(startIndex,endIndex), 1)
    pass
def solveSimple(a):
    if not a:
        return 0
    r = a[0]
    n = len(a)
    for i in range(n):
        for j in range(i,n):
            r = max(r, mulSubList(a, i, j+1))
    return r
def solve(a):
    if not a:
        return 0
    pos = a[:]
    neg = a[:]
    n = len(a)
    for i in range(n-2, -1,-1):
        if a[i] >= 0:
            pos[i] = max(a[i], a[i]*pos[i+1])
            neg[i] = min(a[i], a[i]*neg[i+1])
        else:
            pos[i] = max(a[i], a[i]*neg[i+1])
            neg[i] = min(a[i], a[i]*pos[i+1])
    return max(pos)
class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxProduct(self, A):
        return solve(A)
def sp(a,r):
    assert solve(a) == r
    assert solveSimple(a) ==r
def test():
    assert mul([2,3,4]) == 24
    assert mulSubList([2,3,4],0,3) == 24
    assert mulSubList([2,3,4],1,3) == 12

    sp([],0)
    sp([1],1)
    sp([-1],-1)
    sp([-1,-2],2)
    sp([-1,-2,3],6)
    sp([2,3,-2,4], 6)
    sp([2,3,-2,-2,-4], 24)
    sp([-1, 2, 3], 6)

    for i in range(100):
        a = [randint(-100, 100) for x in range(i)]
        assert solve(a) == solveSimple(a)
    pass