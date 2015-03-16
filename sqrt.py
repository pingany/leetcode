#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random,math
from random import randint
from LeetCodeUtils import *
   
def sqrt(y):
    y = float(y)
    x = max(1, y)
    i = 0
    while x * x - y > 1e-6:
        x = (x * x + y) / (2*x)
        i += 1
        pass
    # print "count ", i
    return x
    pass

def sqrt2(y):
    l = float(0)
    h = max(1, float(y))
    while True:
        m = (h+l)/2
        a = m * m - y
        if abs(a) < 1e-6:
            return m
        elif a > 0:
            h = m
        else:
            l = m
        pass
    assert False
    pass

def sqrtInt(y):
    return int(sqrt(y))
    pass
class Solution:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x):
        return sqrtInt(x)

def sp(*a):
    assert sqrt2(*a[:-1]) - a[-1] < 1e-6
    pass


def test():
    sp(1, 1)
    sp(4, 2)
    sp(9, 3)
    sp(0.25, 0.5)
    sp(0.04, 0.2)

def test2():
    pass
    for i in range(10000):
        x = randint(1, 100000000)
        assert sqrt(x) - math.sqrt(x) < 1e-6
        assert sqrt2(x) - math.sqrt(x) < 1e-6
    pass
def testInt():
    assert sqrtInt(5) == 2
    assert sqrtInt(8) == 2
    assert sqrtInt(9) == 3
    for i in range(10000):
        x = randint(1, 100000000)
        assert sqrtInt(x) == int(math.sqrt(x))
