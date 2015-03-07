#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random
from random import randint
from LeetCodeUtils import *
   
INT_MAX = 0x7FFFFFFF
INT_MIN = -0x80000000
def f(integer):
    minus = integer < 0
    integer = abs(integer)
    s = list(str(integer))
    s.reverse()
    i = int("".join(s))
    i = -i if minus else i
    if i >= INT_MIN and i <= INT_MAX:
        return i
    else:
        return 0
class Solution:
    # @return an integer
    def reverse(self, x):
        return f(x)
def sp(integer, results):
    assert f(integer) == results
    pass
def test():
    sp(0, 0)
    sp(10, 1)
    sp(100, 1)
    sp(-100, -1)
    sp(-123, -321)
    sp(1000000003, 0)
    sp(-1000000003, 0)
    pass