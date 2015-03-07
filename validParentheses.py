#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random
from random import randint
from LeetCodeUtils import *
   
def f(s):
    stack = []
    for x in s:
        if x in '({[':
            stack.append(x)
        else:
            if len(stack) == 0:
                return False
            xx = stack[-1] + x
            if xx not in ('()', '[]', '{}'):
                return False
            stack.pop()
    return len(stack) == 0
    pass

def sp(s, x):
    assert f(s) == x
    pass
def test():
    sp('', True)
    sp('[]', True)
    sp('[[]]', True)
    sp('[()]', True)
    sp('[()()]', True)
    sp('[()[]{{[]}{}}()]', True)
    sp('[', False)
    sp(']', False)
    sp('[(]', False)
    sp('[}]', False)
    pass