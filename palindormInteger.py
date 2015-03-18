#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random
from random import randint
from LeetCodeUtils import *
   
def solve(n):
    if n < 0:
        return False
    low = 10
    high = 1
    while high * 10 <= n:
        high *= 10

    while n > 0:
        i = n / high
        j = n % low
        if i != j:
            return False
        n %= high
        n /= low

        high /= 100
    return True
class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        return solve(x)

def solveSimple(n):
    if n < 0:
        return False
    s = str(n)
    return s == "".join(reversed(s))
def sp(*a):
    assert solve(*a[:-1]) == a[-1]
    pass
def test():
    sp(0, True)
    sp(1, True)
    sp(101, True)
    sp(1001, True)
    sp(1111, True)
    sp(1221, True)
    sp(121, True)
    sp(-121, False)
    sp(12, False)
    sp(21, False)
    sp(1000021, False)
    for i in range(100000):
        x = randint(1, 1000000000)
        sp(x, solveSimple(x))
    pass