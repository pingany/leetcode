#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random
from random import randint
from LeetCodeUtils import *
   
INT_MAX = 2147483647
INT_MIN = -2147483648
def atoi(s):
    i = 0
    n = len(s)
    # ignore spaces
    while i < n and  s[i] == ' ':
        i += 1
    if i >= n:
        return 0
    minus = False
    if s[i] == '-':
        minus = True
        i += 1
    elif s[i] == '+':
        i += 1
        pass
    sum = 0
    while i < n and s[i] in '0123456789':
        sum = sum * 10 + int(s[i])
        i += 1
        if sum > 2147483648:
            sum = 2147483648
            break
    # print sum
    sum = sum if not minus else -sum
    sum = max(sum, INT_MIN)
    sum = min(sum, INT_MAX)
    return sum
class Solution:
    # @return an integer
    def atoi(self, str):
        return atoi(str)
def sp(s, i):
    assert atoi(s) == i
def test():
    sp('', 0)
    sp('         ', 0)
    sp(' ', 0)
    sp(' 123', 123)
    sp(' -123', -123)
    sp(' +123', +123)
    sp(' +123  ', +123)
    sp(' +123  fadfa', +123)
    sp(' +123fasdfa  fadfa', +123)
    sp(' +123123123123123132312  fadfa', INT_MAX)
    sp(' -123123123123123132312  fadfa', INT_MIN)
    pass