#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random
from random import randint
from LeetCodeUtils import *
   
def f(s):
    s = s.strip()
    l = s.split(' ')
    if l:
        return len(l[-1])
    else:
        return 0
    pass
class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        return f(s)
def sp(s, l):
    assert l == f(s)
    pass
def test():
    sp('', 0)
    sp('a', 1)
    sp('a a', 1)
    sp('a a a', 1)
    sp('a a a ', 1)
    sp('a a ab   ', 2)
    pass