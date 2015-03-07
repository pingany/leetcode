#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random
from random import randint
from LeetCodeUtils import *
   
def f(a):
    s = 0
    for x in a:
        s ^= x
    return s
    pass
class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        return f(A)
def sp(a, l):
    assert l == f(a)
    pass
def test():
    sp([], 0)
    sp([1], 1)
    sp([1, 1, 2], 2)
    sp([1, 1, 2, 3, 2], 3)
    pass