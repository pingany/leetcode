#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random
from random import randint
from LeetCodeUtils import *
   
def solve(a):
    n = len(a)
    if not n:
        return 0
    f = a[n-1][:]
    for i in range(n-2, -1, -1):
        for j in range(0, len(a[i])):
            f[j] = a[i][j] + min(f[j], f[j+1])
    return f[0]
    pass
class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        return solve(triangle)
def sp(*a):
    assert solve(*a[:-1]) == a[-1]
    pass
def test():
    sp([], 0)
    sp([[1]], 1)
    sp([[1], [2, 3]], 3)
    sp([
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
], 11)
    pass