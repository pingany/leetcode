#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random
from random import randint
from LeetCodeUtils import *
   
def f(s, nRows):
    if nRows <= 1:
        return s
    i = 0
    rows = [[] for x in range(nRows)]
    downwards = True
    for x in s:
        rows[i].append(x)
        if downwards:
            if i == nRows - 1:
                i -= 1
                downwards = False
            else:
                i += 1
        else:
            if i == 0:
                i += 1
                downwards = True
            else:
                i -= 1
    return "".join(["".join(row) for row in rows])
    pass
class Solution:
    # @return a string
    def convert(self, s, nRows):
        return f(s, nRows)
def sp(s, nRows, results):
    assert f(s, nRows) == results
    pass
def test():
    sp("12", 1, "12")
    sp("", 1, "")
    sp("1234", 2, "1324")
    sp("PAYPALISHIRING", 3, "PAHNAPLSIIGYIR")
    pass