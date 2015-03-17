#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random
from random import randint
from LeetCodeUtils import *
   
def solve(s):
    if not s:
        return 0
    n = len(s)
    f = [0]*(n+1)
    f[n] = 1
    f[n-1] = 1 if s[n-1] != '0' else 0
    for i in xrange(n-2, -1, -1):
        if s[i] != '0':
            f[i] += f[i+1]
            if s[i]+s[i+1] <= '26':
                f[i] += f[i+2]
    return f[0]
class Solution:
    # @param s, a string
    # @return an integer
    def numDecodings(self, s):
        return solve(s)
def sp(*a):
    assert solve(*a[:-1]) == a[-1]
    pass
def test():
    sp("", 0)
    sp("1", 1)
    sp("12", 2)
    sp("27", 1)
    sp("20", 1)
    sp("26", 2)
    sp("96", 1)
    pass