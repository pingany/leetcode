#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random
from random import randint
from LeetCodeUtils import *
   
def solve(x, n):
    r = 1
    minus = n < 0
    n = abs(n)
    while n:
        if n & 1:
            r *= x
        x *= x
        n >>= 1
    return r if not minus else 1.0/r
class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    def pow(self, x, n):
        return solve(x, n)
def sp(*a):
    assert solve(*a[:-1]) == a[-1]
    pass
def test():
    sp(0, 0, 1)
    sp(1, 0, 1)
    sp(2, 0, 1)
    sp(0, 100, 0)
    sp(1, 100, 1)
    sp(2, 1, 2)
    sp(2, 10, 1024)
    sp(2, -10, 1.0/1024)
    sp(2, -1, 1.0/2)
    pass