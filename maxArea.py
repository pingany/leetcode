#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random
from random import randint
from LeetCodeUtils import *
   
def solveSimple(a):
    n = len(a)
    s = 0
    for i in range(n-1):
        for j in range(i+1,n):
            s = max(s, min(a[i],a[j])*(j-i))
    return s
def solve(a):
    n = len(a)
    s = 0
    i = 0
    j = n-1
    while i < j:
        if a[i] <= a[j]:
            s = max(s, (a[i]*(j-i)))
            i +=1
        else:
            s = max(s, a[j]*(j-i))
            j -=1
    return s
class Solution:
    # @return an integer
    def maxArea(self, height):
        return solve(height)
def sp(*a):
    assert solve(*a[:-1]) == a[-1]
    pass
def test():
    sp([], 0)
    sp([1], 0)
    sp([1,2], 1)
    sp([2,2], 2)
    sp([1,2,3,4], 4)
    for x in range(100):
        a = [randint(1,100) for i in range(x)]
        assert solveSimple(a) == solve(a)
    pass