#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random
from random import randint
from LeetCodeUtils import *
   
def solve(nums):
    if not nums:
        return ""
    nums = [str(n) for n in nums]
    def cmpString(x, y):
        s1 = x + y
        s2 = y + x
        return cmp(s1, s2)
    nums.sort(cmp=cmpString,reverse=True)
    s = "".join(nums)
    s = s.lstrip('0')
    if not s:
        s = "0"
    return s
class Solution:
    # @param num, a list of integers
    # @return a string
    def largestNumber(self, num):
        return solve(num)
def sp(*a):
    assert solve(*a[:-1]) == a[-1]
    pass
def test():
    sp([], "")
    sp([1], "1")
    sp([3, 30, 34, 5, 9], "9534330")
    sp([0,0], "0")
    pass