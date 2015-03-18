#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random
from random import randint
from LeetCodeUtils import *
   
def isAllSame(s):
    for i in range(1, len(s)):
        if s[i] != s[i-1]:
            return False
    return True
def solve(strs):
    if not strs:
        return ""
    minLen = min([len(s) for s in strs])
    i = 0
    while i < minLen:
        ps = [s[i] for s in strs]
        if not isAllSame(ps):
            break
        i += 1
    return s[:i]

class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        return solve(strs)
        
def sp(*a):
    assert solve(*a[:-1]) == a[-1]
    pass
def test():
    sp([], "")
    sp([""], "")
    sp(["1",""], "")
    sp(["1","1"], "1")
    sp(["1","12"], "1")
    sp(["1","11"], "1")
    sp(["12","12"], "12")
    pass

