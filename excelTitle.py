#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random
from random import randint
from LeetCodeUtils import *
   
def f(num):
    r = []
    while num > 0:
        if num % 26 == 0:
            r.append('Z')
            num -= 26
        else:
            r.append(chr(num%26 + ord('A')-1))
        num /= 26
    r.reverse()
    return ''.join(r)

class Solution:
    # @return a string
    def convertToTitle(self, num):
        return f(num)
def sp(x, y):
    assert f(y) == x
    pass
def test():
    sp('A', 1)
    sp('B', 2)
    sp('Z', 26)
    sp('AA', 27)
    sp('AB', 28)
    sp('ZZ', 26*26+26)
    sp('ZA', 26*26+1)
    sp('AZ', 1*26+26)
    sp('ZZZ', 26*26*26+26*26+26)
    pass