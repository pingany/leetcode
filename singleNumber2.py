#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random
from random import randint
from LeetCodeUtils import *
   
# x to ３进制list,第一位表示符号，１标示负数
def div3(x, list):
    list.append(1 if x < 0 else 0)
    x = abs(x)
    while x:
        list.append(x%3)
        x /=3

def addSpecial(l, t):
    n = min(len(l), len(t))
    i = 0
    while i < n:
        l[i] = (l[i] + t[i]) % 3
        i += 1

    nt = len(t)
    if n < nt:
        i = n
        while i < nt:
            l.append(t[i])
            i += 1
            pass
    pass
def f(a):
    l = [0]
    t = []
    for x in a:
        del t[:]
        div3(x, t)
        addSpecial(l, t)
    s = 0
    i = len(l) -1 
    while i >= 1:
        s = s * 3 + l[i]
        i -= 1
    return s if l[0] == 0 else -s
    pass
class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        return f(A)
def sp(a, x):
    assert x == f(a)
    pass
def testMinus():
    sp([-1], -1)
    pass
def test():
    sp([], 0)
    sp([1], 1)
    sp([2], 2)
    sp([100], 100)
    sp([100, 100, 100, 323213], 323213)
    sp([-2,-2,1,1,-3,1,-3,-3,-4,-2], -4)
    pass