#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random
from random import randint
from LeetCodeUtils import *
     

def f1(prices, start, n):
    profit = 0
    maxs = [0]*(n+1)
    for i in range(n-1, -1, -1):
        maxs[i] = max(prices[i+start], maxs[i+1])
    for i in range(n-1):
        profit = max(profit, maxs[i+1]-prices[i+start])
    return profit

def fSimple(prices):
    n = len(prices)
    a = [f1(prices, 0, k) + f1(prices, k, n-k) for k in range(0, n+1)]
    return max(a)
def array2(row, col, initValue=None):
    return [[initValue for x in range(col)] for x in range(row)] 

def fNotLimited(prices):
    s = 0
    for i in range(1, len(prices)):
        x = prices[i]-prices[i-1]
        if x > 0:
            s += x
    return s
def f(prices, maxCount):
    n = len(prices)
    if not n or maxCount <= 0:
        return 0
    if maxCount > n/2:
        return fNotLimited(prices)
    f = array2(n, maxCount+1)
    g = array2(n, maxCount+1)
    for i in range(n):
        f[i][0] = 0
        g[i][0] = 0
    for k in range(0, maxCount+1):
        f[0][k] = 0
        g[0][k] = 0
    for k in range(1, maxCount+1):
        for i in range(1, n):
            diff = prices[i] - prices[i-1]
            f[i][k] = max(f[i-1][k]+diff, g[i-1][k-1]+max(0, diff))
            g[i][k] = max(f[i][k], g[i-1][k])
    return g[n-1][maxCount]

class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, k, prices):
        return f(prices, k)
def sp(prices, k, y):
    assert f(prices, k) == y

def testR():
    for i in range(1, 100):
        prices = [randint(1, 100) for x in range(i)]
        assert f(prices,2) == fSimple(prices)
        f(prices, 10)
def test11():
    sp([11, 55], 2, 44)
def test():
    sp([], 2,  0)
    sp([1],2,  0)
    sp([1, 2],2, 1)
    sp([1, 0],2, 0)
    sp([1, 2, 3, 4],2, 3)
    sp([1, 2, -1, 4],2, 6)

def testBig():
    f(range(10000, 0, -1),2)
def test2():
    k, prices = json.load(open("bestTimeToBuySellStock4.in"))
    print len(prices)
    f(prices,k)
    pass