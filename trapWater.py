#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random
from random import randint
from LeetCodeUtils import *
   
def stripList(a, toStrip):
    i = 0
    j = len(a)-1
    while i <= j && a[i] == toStrip:
        i += 1
    while j >= i && a[j] == toStrip:
        j -= 1
    return a[i:j+1]

def solve(a):
    a = stripList(a)
    while len(a):
        for k in range(i+1, len(a)):
            if a[k] >= a[i]:
                water = (k-i)*a[i] - sum(a[i+1:k])
                assert water >= 0
                r += water
                i = k
        if i < len(a)-1:
            a = a[i:]
            a.reverse()
        pass
    pass
def sp(*a):
    assert solve(*a[:-1]) == a[-1]
    pass
def test():
    assert stripList([0,0,1,0], [1])
    sp([0,1,0,2,1,0,1,3,2,1,2,1], 6)
    pass