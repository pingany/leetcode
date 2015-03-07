#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random
from random import randint
from LeetCodeUtils import *

def reverse(list, s, e):
    while s < e:
        list[s], list[e] = list[e], list[s]
        s += 1
        e -= 1
        pass
    pass
def f(nums, k):
    n = len(nums)
    if not n:
        return
    k %= n
    reverse(nums, 0, n-k-1)
    reverse(nums, n-k, n-1)
    reverse(nums, 0, n-1)
    pass
class Solution:
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.
    def rotate(self, nums, k):
        f(nums, k)

def sp(nums, k, results):
    f(nums, k)
    assert nums == results
    pass
def test():
    sp([], 1, [])
    sp([1], 1, [1])
    sp([1, 2], 1, [2, 1])
    sp([1, 2], 2, [1, 2])
    sp([1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1,2, 3,4])
    sp([1,2 ], 3, [2, 1])
    pass