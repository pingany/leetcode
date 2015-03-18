#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random
from random import randint
from LeetCodeUtils import *

def removeElement(a,e):
    k = 0
    for x in a:
        if x != e:
            a[k] = x
            k += 1 
    return k
class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        return removeElement(a, elem)
def sp(a,e, expected):
    k = removeElement(a, e)
    assert e not in expected
    assert a[:k] == expected
def test():
    sp([], 1, [])
    sp([2,3], 1, [2,3])
    sp([2,3], 2, [3])
    sp([2,3,2], 2, [3])
    sp([2,3,2], 3, [2,2])
    pass