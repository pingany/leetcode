#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random
from random import randint
from LeetCodeUtils import *
   
def say(a):
    n = len(a)
    results = []
    k = 1
    for i in range(1, n):
        if a[i] == a[i-1]:
            k+=1
            continue
        results.append(k)
        results.append(a[i-1])
        k = 1
    results.append(k)
    results.append(a[n-1])
    return "".join([str(x) for x in results])

def solve(n):
    r = "1"
    for i in xrange(1, n):
        r = say(r)
    return r

class Solution:
    # @return a string
    def countAndSay(self, n):
        return solve(n)

def sp(*a):
    assert solve(*a[:-1]) == a[-1]
    pass
def test():
    sp(1, '1')
    sp(2, '11')
    sp(3, '21')
    sp(4, '1211')
    sp(5, '111221')
    pass
