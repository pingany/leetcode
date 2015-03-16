#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random
from random import randint
from LeetCodeUtils import *
   
MAX_INT = 0x7FFFFFFF

def solveWithMul(y, x):
    l = 0
    h = MAX_INT
    while l < h:
        m = (l + h + 1) >> 1
        if x * m <= y:
            l = m
        else:
            h = m-1
    return l
    pass


MAX_INT = 0x7FFFFFFF
MIN_INT = -0x80000000
def solve(y, x):
    if not x:
        return MAX_INT if y >= 0 else MIN_INT
    minus = False
    if (x>=0) != (y >=0):
        minus = True
    x = abs(x)
    y = abs(y)

    a = x
    mul = 1
    while (a << 1) <= y:
        a <<= 1
        mul <<= 1
    s = 0
    while y >= x:
        if y >= a:
            y -= a
            s += mul
        a >>= 1
        mul >>= 1
    if minus:
        s = -s
    return min(MAX_INT, max(s, MIN_INT))
    pass
class Solution:
    # @return an integer
    def divide(self, dividend, divisor):
        return solve(dividend, divisor)

def sp(*a):
    assert solve(*a[:-1]) == a[-1]
    pass

def div(y, x):
    if not x:
        return MAX_INT if y >= 0 else MIN_INT
    minus = y/x < 0
    a = abs(y)/abs(x)
    return -a if minus else a

def test1():
    assert solve(459, 7) == 65
    assert solve(2, 1) == 2
    assert solve(-2147483648, -1) == MAX_INT
    pass
def test():
    for i in range(10000):
        x = randint(-100, 100)
        y = randint(-1000, 1000)
        assert solve(y, x) == div(y, x)
    pass