#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random,bisect
from random import randint
from LeetCodeUtils import *
   
def f(a):
    a = sorted(a)
    n = len(a)
    result = []
    for i in range(n-2):
        if i > 0 and a[i] == a[i-1]:
            continue
        for j in range(i+1, n-1):
            if j > i+1 and a[j] == a[j-1]:
                continue
            left = 0 - a[i] - a[j]
            k = bisect.bisect_left(a, left, j+1)
            if k != n and a[k] == left:
                result.append([a[i], a[j], a[k]])
            elif k == j+1:
                break
    return result

class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        return f(num)

def sp(a, r):
    assert f(a) == sorted(r)
def test():
    sp([], [])
    sp([1], [])
    sp([1, 2], [])
    sp([1, 2, 3], [])
    sp([1, 2, -3], [[-3, 1, 2]])
    sp([-1, 0, 1, 2, -1, -4], [[-1, 0, 1], [-1, -1, 2]])
    sp([-1, -1, -1, 2, 2], [[-1, -1, 2]])
    sp([0, 0, 0, 0, 0, 0, 0], [[0, 0, 0]])
    sp([0, 0, 0, 0, 0, 1, -1], [[0, 0, 0], [-1, 0, 1]])
    pass