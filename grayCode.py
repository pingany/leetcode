#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random
from random import randint
from LeetCodeUtils import *

def solve(n):
    if n <= 0:
        return [0]
    result = [0, 1]
    for i in xrange(2, n+1):
        toAdd = 1 << (i-1)
        for x in reversed(result):
            result.append(x+toAdd)
    return result
class Solution:
    # @return a list of integers
    def grayCode(self, n):
        return solve(n)

def sp(*a):
    assert solve(*a[:-1]) == a[-1]
    pass
def test():
    sp(0, [0])
    sp(1, [0, 1])
    sp(2, [0, 1, 3, 2])
    sp(3, [0, 1, 3, 2, 6, 7, 5, 4])
    pass