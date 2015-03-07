#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random
from random import randint
from LeetCodeUtils import *

def f(a):
    n = len(a)
    if n < 2:
        return a[0]
    l = 0
    h = n-1
    while l <= h:
        if a[l] < a[h]:
            return a[l]
        m = (l+h)/2
        if a[m] < a[l]:
            h = m
        else:
            l = m+1
    return a[h]

class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        return f(num)
def sp(a, x):
    assert f(a) == x
    pass
def test():
    sp([1], 1)
    sp([1, 2], 1)
    sp([2, 1], 1)
    for i in range(1, 100):
        a = [randint(1, 100) for x in range(i)]
        a.sort()
        x = randint(0, len(a))
        a = a[:x] + a[x:]
        assert f(a) == min(a)
    pass