#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random
from random import randint
from LeetCodeUtils import *
   
def f(a):
    l = 0
    h = len(a) -1
    while l < h:
        m = (l+h)/2
        if m == l:
            if a[m] > a[m+1]:
                return m
            l = m+1
        elif m == h:
            if a[m] > a[m-1]:
                return m
            h = m-1
        else:
            if a[m] > a[m+1] and a[m] > a[m-1]:
                return m
            elif a[m] < a[m+1]:
                l = m+1
            else:
                assert a[m] < a[m-1]
                h = m-1
    return l

def sp(a):
    x = f(a)
    a.insert(0, -1000)
    a.append(-1000)
    x += 1
    assert a[x] > a[x-1] and a[x] > a[x+1]
def testR():
    for i in range(1, 1000):
        a = range(i)
        random.shuffle(a)
        sp(a)

def test():
    assert f([]) == 0
    sp([1])
    sp([1, 2])
    sp([2, 1])
    pass