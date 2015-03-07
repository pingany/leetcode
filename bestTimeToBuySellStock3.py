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

def f(prices):
    n = len(prices)
    if not n:
        return 0
    maxFrom = [None]*n
    minTo = [None]*n

    maxFrom[n-1] = prices[n-1]
    minTo[0] = prices[0]
    for i in range(n-2, -1, -1):
        maxFrom[i] = max(maxFrom[i+1], prices[i])

    for i in range(1, n):
        minTo[i] = min(minTo[i-1], prices[i])

    buy = [None]*n
    sell = [None]*n
    buy[n-1] = 0
    for i in range(0, n-1):
        buy[i] = maxFrom[i+1] - prices[i]

    sell[0] = 0
    for i in range(1, n):
        sell[i] = prices[i] - minTo[i-1]

    maxSell = [None]*n
    maxSell[0] = sell[0]
    for i in range(1, n):
        maxSell[i] = max(maxSell[i-1], sell[i])

    maxBuy = [None]*(n+1)
    maxBuy[n-1] = buy[n-1]
    for i in range(n-2, -1, -1):
        maxBuy[i] = max(maxBuy[i+1], buy[i])

    maxBuy[n] = 0
    a = [maxSell[k] + maxBuy[k+1] for k in range(0, n)]
    return max(a)

class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        return f(prices)
def sp(x, y):
    assert f(x) == y

def testR():
    for i in range(1, 100):
        prices = [randint(1, 100) for x in range(i)]
        assert f(prices) == fSimple(prices)
def test():
    sp([], 0)
    sp([1], 0)
    sp([1, 2], 1)
    sp([1, 0], 0)
    sp([1, 2, 3, 4], 3)
    sp([1, 2, -1, 4], 6)

def testBig():
    f(range(10000, 0, -1))
def test2():
    prices = json.load(open("stock2.in"))
    print len(prices)
    f(prices)
    pass