#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random
from random import randint
from LeetCodeUtils import *
   
def f(a, b):
    def convert(a):
        l = [int (x) for x in a]
        l.reverse()
        return l
        pass
    a = convert(a)
    b = convert(b)
    na = len(a)
    nb = len(b)
    n = max(na, nb)
    c = 0
    r = []
    for i in range(n):
        x = c
        if i < na:
            x += a[i]
        if i < nb:
            x += b[i]
        c = x / 2
        r.append(x%2)
    if c:
        r.append(c)
    r.reverse()
    return "".join([str(x) for x in r])
class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        return f(a, b)

def sp(x, y, z):
    assert f(x,y ) == z
    pass
def test():
    sp("0", "1", "1")
    sp("0", "0", "0")
    sp("11", "0", "11")
    sp("0", "11", "11")
    sp("1", "11", "100")
    sp("11", "11", "110")
    pass