#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random,bisect
from random import randint
from LeetCodeUtils import *
   
   
def absMin(x, y):
    return x if abs(x) < abs(y) else y

def f(a, target):
    n = len(a)
    if n < 3:
        return 0
    a = sorted(a)
    gap = (1 << 30)
    for i in range(n-2):
        if i > 0 and a[i] == a[i-1]:
            continue
        for j in range(i+1, n-1):
            if j > i+1 and a[j] == a[j-1]:
                continue
            left = target - a[i] - a[j]
            start = j +1
            k = bisect.bisect_left(a, left, start)
            if k != n and a[k] == left:
                return target
            if k < n:
                gap = absMin(gap, a[k]-left)
            if k < n -1:
                gap = absMin(gap, a[k+1]-left)
            if k > start:
                gap = absMin(gap, a[k-1]-left)
            if k == start:
                break
    return target + gap
class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
        return f(num, target)

def sp(x, y, z):
    assert f(x,y) == z
def test():
    sp([-1, 2, 1, -4], 1, 2)
    sp([], 1100, 0)
    sp([1], 1100, 0)
    sp([1,2], 1100, 0)
    sp([1,2,3], 10, 6)
    sp([1,1,1], 10, 3)
    sp([1, 2, 3, 4],10, 9)
    sp([-1, -2, -3, -4],-10, -9)
    sp([-1, -2, -3, -4],10, -6)
    sp([1,1,1,2,2,2,3,3,3], 6, 6)
    pass