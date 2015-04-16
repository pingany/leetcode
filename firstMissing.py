#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random
from random import randint
from LeetCodeUtils import *
   
def solve(a):
    i = 0
    n = len(a)
    while i < n:
        if not (a[i] > 0 and a[i] < n+1):
            a[i] = 0
        elif a[i] != i + 1:
            if a[a[i]-1] != a[i]:
                a[a[i]-1], a[i] = a[i], a[a[i]-1]
                continue
            else:
                a[i] = 0
        i += 1
    for i in range(n):
        if a[i] == 0:
            return i+1
    return n+1
class Solution:
    # @param nums, an integer[]
    # @return an integer
    def firstMissingPositive(self, nums):
        return solve(nums)
def sp(*a):
    assert solve(*a[:-1]) == a[-1]
    pass
def test():
    sp([1,2,0], 3)
    sp([1,2,3], 4)
    sp([3,4,-1,1],2)
    sp([3,4,-1,1],2)
    sp([3,4,3,1],2)
    sp([3,4,1,4],2)
    pass