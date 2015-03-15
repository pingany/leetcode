#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random
from random import randint
from LeetCodeUtils import *
   
def solveBest(n):
    i = 0
    while n:
        n &= n-1
        i += 1
        pass
    return i
    pass

def solve(n):
    i = 0
    while n:
        if (n & 1):
            i += 1
        n >>= 1
        pass
    return i
class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        return solve(n)
def sp(*a):
    assert solve(*a[:-1]) == a[-1]
    pass
def test():
    sp(0, 0)
    sp(1, 1)
    sp(2, 1)
    sp(3, 2)
    sp(4, 1)
    sp(5, 2)
    pass