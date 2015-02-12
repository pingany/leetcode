#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random,bisect
from random import randint
from LeetCodeUtils import *
   
def f(a,target):
    a.sort()
    # a = sorted(a)
    n = len(a)
    result = []
    for i in xrange(n-3):
        if i > 0 and a[i] == a[i-1]:
            continue
        for j in xrange(i+1, n-2):
            if j > i+1 and a[j] == a[j-1]:
                continue
            h = j+1-1
            while h < n-1-1:
                h += 1
                if h > j+1 and a[h] == a[h-1]:
                    continue
                left = target - a[i] - a[j] - a[h]
                start = h+1
                k = bisect.bisect_left(a, left, start)
                if k != n and a[k] == left:
                    result.append([a[i], a[j], a[h], a[k]])
                elif k == start:
                    break
    return result

class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def fourSum(self, num, target):
        return f(num,target)
def sp(a, r):
    assert f(a, 0) == sorted(r)
def test():
    sp([], [])
    sp([1], [])
    sp([1, 2], [])
    sp([1, 2, 3], [])
    sp([1, 2, -3, 0], [[-3, 0, 1, 2]])
    sp([-1, 0, 1, 2, -1, -4, 0], [[-1, 0, 0, 1], [-1, -1, 0, 2]])
    sp([-1, -1, -1, 2, 2, 0], [[-1, -1, 0, 2]])
    sp([0, 0, 0, 0, 0, 0, 0], [[0, 0, 0, 0]])
    sp([0, 0, 0, 0, 0, 1, -1], [[0, 0, 0, 0], [-1, 0, 0, 1]])

def test2():
    a, target = json.load(open("4sum.in"))
    print len(a),target
    f(a, target)
    pass