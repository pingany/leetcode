#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random
from random import randint
from LeetCodeUtils import *
   
def solve(a):
    n = len(a)
    assert n > 0
    f = [False]*n
    f[n-1] = True
    for i in range(n-2,-1,-1):
        if f[i+1]:
            f[i] = a[i] >= 1
        else:
            for j in range(i+1+a[i+1]+1, min(n, i+a[i]+1)):
                if f[j]:
                    f[i] = True
                    break
    return f[0]
class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        return solve(A)
def sp(*a):
    assert solve(*a[:-1]) == a[-1]
    pass
def test():
    sp([1], True)
    sp([0], True)
    sp([1,2], True)
    sp([0,2], False)
    sp([2,3,1,1,4], True)
    sp([3,2,1,0,4], False)
    pass