#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random
from random import randint
from LeetCodeUtils import *
   
def solve(n):
    s = 0
    for i in range(32):
        s = (s << 1) + (n& 1)
        n >>=1
    return s
def solveSimple(n):
    bits = []
    for i in range(32):
        bits.append(n & 1)
        n >>= 1
    s = 0
    for x in bits:
        s = (s << 1) + x
    return s
    pass
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        return solve(n)
def sp(*a):
    assert solve(*a[:-1]) == a[-1]
    assert solveSimple(*a[:-1]) == a[-1]
    pass
def test():
    sp(1, 2147483648)
    sp(0, 0)
    sp(2147483648, 1)
    sp((1<<30), (1 << 1))
    for i in range(1000):
        x = randint(0, 10000000)
        sp(x, solveSimple(x))
    pass