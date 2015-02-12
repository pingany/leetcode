#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random
from random import randint
from LeetCodeUtils import *
   
def f(s):
    r = 0
    for x in s:
        r = r * 26 + (ord(x) - ord('A') + 1)
    return r
class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
        return f(s)
def sp(x, y):
    assert f(x) == y
    pass
def test():
    sp('', 0)
    sp('A', 1)
    sp('B', 2)
    sp('AA', 27)
    sp('AB', 28)
    pass