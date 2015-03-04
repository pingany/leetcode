#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random,math
from random import randint
from LeetCodeUtils import *

def f(a):
    if not a or len(a) < 2:
        return 0
    minElement = min(a)
    a = [x - minElement for x in a]
    B = max(a)
    n = len(a)
    bulletSize = int(math.ceil((float(B)/(n-1))))
    if bulletSize == 0:
        return 0
    bulletNum = B/bulletSize + 1
    bullets = [None] * bulletNum
    for x in a:
        index = x/bulletSize
        if bullets[index] is None:
            bullets[index] = [x, x]
        else:
            b = bullets[index]
            bullets[index] = [min(b[0], x), max(b[1], x)]
    bullets = [x for x in bullets if x]
    r = 0
    for i in range(1, len(bullets)):
        r = max(r, bullets[i][0] - bullets[i-1][1])
    return r

class Solution:
    # @param num, a list of integer
    # @return an integer
    def maximumGap(self, num):
        return f(num)

def sp(a, r):
    assert f(a) == r
    pass

def f2(a):
    n = len(a)
    if n < 2:
        return 0
    a = sorted(a)
    r = 0
    for i in range(1, n):
        r = max(r, a[i]-a[i-1])
    return r

def testR():
    for i in range(1, 100):
        a = [randint(1, 100) for x in range(i)]
        assert f(a) == f2(a)

def test():
    sp([], 0)
    sp([1], 0)
    sp([0, 1], 1)
    sp([1, 1], 0)
    sp([1, 1, 2], 1)
    sp([2, 3, 0], 2)
    pass