#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random
from random import randint
from LeetCodeUtils import *
   
def solve(a):
    i = 0
    j = len(a)-1
    while i <= j and a[i] == 0:
        i += 1
        pass
    while j >= i and a[j] == 2:
        j -= 1
        pass

    k = i
    while k <= j:
        if a[k] == 0:
            a[i], a[k] = a[k], a[i]
            i += 1
            k = max(i, k)
        elif a[k] == 2:
            a[j], a[k] = a[k], a[j]
            j -= 1
        else:
            k += 1
            pass
        pass
    pass
class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        solve(A)
def sp(a):
    origin = a[:]
    solve(a)
    assert sorted(origin) == a
    pass
def test1():
    sp([2, 2, 2, 0])
    pass
def test():
    sp([])
    sp([0])
    sp([1])
    sp([2])
    sp([2, 1])
    sp([1, 0, 2, 0])
    sp([1, 2, 0, 1, 2, 0])
    for i in range(1000):
        x = [randint(0, 2) for l in range(i)]
        sp(x)
    pass