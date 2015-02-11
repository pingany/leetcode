#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random
from random import randint
from LeetCodeUtils import *

ff = [None]*(1000+1)
ff[0] = [[]]

def mul(l1, l2):
    m = len(l1)
    n = len(l2)
    results = []
    for i in range(m):
        for j in range(n):
            results.append(['('] + l1[i]+ [')'] + l2[j])
    return results

def f(n):
    if not ff[n]:
        for i in range(1, n+1):
            ff[i] = []
            for j in range(i-1, -1, -1):
                left = ff[j]
                right = ff[i-1-j]
                ff[i] += mul(left, right)
    return ["".join(x) for x in ff[n]]
class Solution:
    # @param an integer
    # @return a list of string
    def generateParenthesis(self, n):
        return f(n)

def sp(x, y):
    assert (f(x)) == (y)
def test():
    sp(0, [""])
def test1():
    sp(1, ["()"])

def test3():
    sp(3, ["((()))", "(()())", "(())()", "()(())", "()()()"])
    for i in range(13):
        f(i)
    pass