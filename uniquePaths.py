#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random
from random import randint
from LeetCodeUtils import *

def array2(row, col, initValue=None):
    return [[initValue for x in range(col)] for x in range(row)] 

def solve(m, n):
    assert m > 0 and n > 0
    rows = n
    cols = m
    f = array2(rows, cols, 1)
    for i in xrange(rows-2, -1, -1):
        for j in xrange(cols-2, -1, -1):
            f[i][j] = f[i+1][j] + f[i][j+1]
    return f[0][0]
class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
        return solve(m, n)
def sp(*a):
    assert solve(*a[:-1]) == a[-1]
    pass
def test():
    sp(1, 1, 1)
    sp(1, 100, 1)
    sp(100, 1, 1)
    sp(2, 2, 2)
    pass