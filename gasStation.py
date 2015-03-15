#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random
from random import randint
from LeetCodeUtils import *
   
diff = []
def next(i):
    return (i+1) % (len(diff))
    pass
def prev(i):
    n = len(diff)
    return (i+n-1) % n 
    pass
def solve(diff2):
    global diff
    diff = diff2
    n = len(diff)
    if n <= 0:
        return -1
    elif n == 1:
        return 0 if diff[0] >= 0 else -1 

    i = 0
    while i < n and diff[i] < 0:
        i +=1
        pass
    if i == n:
        return -1
    assert diff[i] >= 0

    sum = diff[i]
    j = i
    while True:
        while sum >= 0:
            j = next(j)
            if j == i:
                return i
            sum += diff[j]
            pass
        while sum < 0:
            i = prev(i)
            if i == j:
                return -1
            sum += diff[i]
            pass
        pass
    pass

def solve2(gas, cost):
    return solve([gas[i] - cost[i] for i in range(len(gas))])
class Solution:
    # @param gas, a list of integers
    # @param cost, a list of integers
    # @return an integer
    def canCompleteCircuit(self, gas, cost):
        return solve2(gas, cost)

def sp(*a):
    assert solve(*a[:-1]) == a[-1]
    pass
def test():
    sp([], -1)
    sp([1], 0)
    sp([0], 0)
    sp([-1], -1)
    sp([-1, -2, 3], 2)
    sp([-1, -2, -3], -1)
    sp([1, 2, -3, -4, 4, 3], 4)
    sp([1, 2, -3, -4, 1, 3], 4)
    sp([1, 2, -3, -4, -1, 3], -1)
    pass