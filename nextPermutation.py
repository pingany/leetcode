#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random
from random import randint
from LeetCodeUtils import *
   
def reverse(a, start, end):
    i = start
    j = end-1
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1
def solve(a):
    if len(a) < 2:
        return
    n = len(a)
    i = n-1
    while i > 0:
        if a[i] > a[i-1]:
            break
        i -= 1
    if i == 0:
        a.reverse()
        return
    lower = i-1
    j = i
    while j < n:
        if a[j] <= a[lower]:
            break
        j += 1
    j -= 1
    # print i,j,lower
    a[lower], a[j] = a[j], a[lower]
    reverse(a, lower+1, n)
class Solution:
    # @param num, a list of integer
    # @return nothing (void), do not return anything, modify num in-place instead.
    def nextPermutation(self, num):
        solve(num)
def solveSimple(a):
    a = a[:]
    if len(a) < 2:
        return a
    n = len(a)
    i = n-1
    while i > 0:
        if a[i] > a[i-1]:
            break
        i -= 1
    if i == 0:
        a.sort()
        return a
    lower = i-1
    c = min([x for x in a[i:] if x > a[lower]])
    b = a[i:]
    b.remove(c)
    b.append(a[lower])
    b.sort()

    a[lower] = c
    a[lower+1:] = b
    return a
def sp(origin, expected):
    a = origin[:]
    solve(a)
    assert a == expected
    # assert solveSimple(origin) == expected
def test():
    sp([],[])
    sp([1],[1])
    sp([1,2], [2,1])
    sp([1,1], [1,1])
    sp([1,2,3], [1,3,2])
    sp([3,2,1], [1,2,3])
    sp([1,1,5], [1,5,1])
    sp([4,1,3,2,1], [4,2,1,1,3])

    for x in xrange(1,1000):
        a = [randint(1, 100) for i in range(x)]
        sp(a, solveSimple(a))
        pass
    pass