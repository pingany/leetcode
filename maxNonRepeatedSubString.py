#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random
from random import randint
from LeetCodeUtils import *
   
def solve(s):
    # print "s", s
    if not s:
        return 0
    n = len(s)
    lastPosition = {}
    maxLength = [None]*n
    for i in xrange(n):
        maxLength[i] = n - i
    for i in xrange(n):
        c = s[i]
        if c in lastPosition:
            p = lastPosition[c]
            maxLength[p] = min(maxLength[p+1]+1, i-p)
        lastPosition[c] = i
    # print maxLength
    for i in xrange(n-2, -1, -1):
        maxLength[i] = min(maxLength[i], maxLength[i+1]+1)
    return max(maxLength)
class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        return solve(s)

def hasNoRepeat(s):
    count = {}
    for x in s:
        if x in count:
            return False
        count[x] = 1
    return True
def solveSimple(s):
    if not s:
        return 0
    n = len(s)
    maxLength = 1
    for i in range(n-1):
        for j in range(i+1, n):
            subs = s[i:j+1]
            if hasNoRepeat(subs):
                maxLength = max(maxLength, j-i+1)
    return maxLength
    pass
def sp(*a):
    assert solveSimple(*a[:-1]) == a[-1]
    assert solve(*a[:-1]) == a[-1]
    pass
def test1():
    sp('tieldmmiltntd', 6)
    sp("bacbbbbc", 3)
    pass
def test():
    sp("", 0)
    sp('a', 1)
    sp("bbbbb", 1)
    sp("bbbbbc", 2)
    sp("abcadae", 4)
    strings = "abcdefghijklmnopqrst"
    n = len(strings)
    for i in range(100):
        s = "".join([strings[randint(0,n-1)] for x in range(i)])
        sp(s, solveSimple(s))
    pass