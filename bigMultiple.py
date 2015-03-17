#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random
from random import randint
from LeetCodeUtils import *
   
def solve(a, b):
    a = [int(x) for x in reversed(a)]
    b = [int(x) for x in reversed(b)]
    la = len(a)
    lb = len(b)
    r = [0]*(la+lb)
    for i in range(lb):
        for j in range(la):
            r[i+j] += b[i] * a[j]

    c = 0
    for i in range(len(r)):
        r[i] += c
        c = r[i] / 10
        r[i] %= 10
    s = "".join([str(x) for x in reversed(r)])
    s = s.lstrip('0')
    if not s:
        s = "0"
    return s
class Solution:
    # @param num1, a string
    # @param num2, a string
    # @return a string
    def multiply(self, num1, num2):
        return solve(num1, num2)
def sp(a, b):
    assert str(a*b) == solve(str(a), str(b))
    assert str(a*b) == solve(str(b), str(a))
def test():
    sp(0, 0)
    sp(0, 1)
    sp(0, 9999)
    sp(1, 9999)
    sp(12, 12)
    sp(99, 99)
    for i in range(10000):
        sp(randint(1,10000000), randint(1, 10000000))
    pass