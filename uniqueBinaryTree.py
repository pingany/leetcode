#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random
from random import randint
from LeetCodeUtils import *
   
f = [1, 1, 2]

def uniqueTreesCount(n):
    global f
    if len(f) < n+1:
        f += [None]*(n+1-len(f))
        assert n+1 == len(f)
    else:
        return f[n]
    for k in xrange(2, n+1):
        s = 0
        for i in range(k):
            s += f[i] * f[k-1-i]
        f[k] = s
    return f[n]
class Solution:
    # @return an integer
    def numTrees(self, n):
        return uniqueTreesCount(n)
def sp(n, results):
    assert results == uniqueTreesCount(n)
    pass
def test():
    sp(0, 1)
    sp(1, 1)
    sp(2, 2)
    sp(3, 5)
    for i in range(4, 100):
        uniqueTreesCount(i)
    pass