#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random
from random import randint
from LeetCodeUtils import *
   
def solve(a, b):
    if len(a) < len(b):
        a,b = b,a
    m = len(a)
    n = len(b)
    lo = 0
    hi = m
    while lo < hi:
        mid = (lo + hi)/2

        posInB = bisect.bisect_left
        pass
    pass
def sp(*a):
    assert solve(*a[:-1]) == a[-1]
    pass
def test():
    pass