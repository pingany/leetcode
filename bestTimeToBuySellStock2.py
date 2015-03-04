#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random
from random import randint
from LeetCodeUtils import *
   
def f(prices):
    n = len(prices)
    ff = [0]*(n+1)
    ff[n] = 0
    for i in range(n-2, -1, -1):
        for j in range(i+1, n+1):
            ff[i] = max(ff[i], ff[j] + prices[j-1]-prices[i])
    return ff[0]
class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        return f(prices)
def sp(x, y):
    assert f(x) == y
def test():
    sp([], 0)
    sp([1], 0)
    sp([1, 2], 1)
    sp([1, 0], 0)
    sp([1, 2, 3, 4], 3)
    sp([1, 2, -1, 4], 6)

def test2():
    prices = json.load(open("stock2.in"))
    print len(prices)
    f(prices)
    pass