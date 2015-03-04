#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random
from random import randint
from LeetCodeUtils import *
   
def f(prices):
    n = len(prices)
    profit = 0
    maxs = [0]*(n+1)
    for i in range(n-1, -1, -1):
        maxs[i] = max(prices[i], maxs[i+1])
    for i in range(n-1):
        profit = max(profit, maxs[i+1]-prices[i])
    return profit
class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        return f(prices)
def sp(x, y):
    assert f(x) == y
    pass
def test():
    sp([],0)
    sp([1],0)
    sp([1,1],0)
    sp([1,2],1)
    sp([2,1],0)
    sp([0, 1, 2, 3], 3)
    pass