#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random,bisect
from random import randint
from LeetCodeUtils import *
   
def solveWithBisect(a, target):
    left = bisect.bisect_left(a, target)
    if left < len(a) and a[left] == target:
        right = bisect.bisect_right(a, target)
        return [left, right-1]
    else:
        return [-1, -1]
    pass
class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        return solveWithBisect(A, target)
def sp(*a):
    assert solveWithBisect(*a[:-1]) == a[-1]
    pass
def test():
    sp([], 0, [-1,-1])
    sp([], 100, [-1,-1])
    sp([1], 0, [-1,-1])
    sp([1], 1, [0, 0])
    sp([1,1], 1, [0, 1])
    sp([0, 1,1], 1, [1, 2])
    sp([5, 7, 7, 8, 8, 10], 8, [3, 4])
    pass