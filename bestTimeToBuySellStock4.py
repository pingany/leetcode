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

prices = None
maxBuy = None

def getMaxBuy(n, k):
    if maxBuy[n] is not None:
        return maxBuy[n][k]
    maxFrom = [None]*n

    maxFrom[n-1] = prices[n-1]
    for i in range(n-2, -1, -1):
        maxFrom[i] = max(maxFrom[i+1], prices[i])

    buy = [None]*n
    sell = [None]*n
    buy[n-1] = 0
    for i in range(0, n-1):
        buy[i] = maxFrom[i+1] - prices[i]

    maxBuy[n] = [None]*(n+1)
    maxBuy[n][n] = 0
    maxBuy[n][n-1] = buy[n-1]
    for i in range(n-2, -1, -1):
        maxBuy[n][i] = max(maxBuy[n][i+1], buy[i])
    return maxBuy[n][k]

def fMaxCount(prices, n, maxCount, store):
    if n <= 0 or maxCount <= 0:
        return 0
    if store[n][maxCount] is not None:
        return store[n][maxCount]

    a = [fMaxCount(prices, k, maxCount-1,store) + getMaxBuy(n, k) for k in range(0, n+1)]
    store[n][maxCount] = b = max(a)
    return b

def array2(row, col, initValue=None):
    return [[initValue for x in range(col)] for x in range(row)] 

def f(prices1, k):
    global prices
    global maxBuy
    prices = prices1
    n = len(prices)
    maxBuy = [None]*(n+1)
    store = array2(n+1, k+1, None)
    return fMaxCount(prices, n, k, store)
class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, k, prices):
        return f(prices, k)
def sp(x, k, y):
    assert f(x, k) == y

def testR():
    for i in range(1, 100):
        prices = [randint(1, 100) for x in range(i)]
        assert f(prices,2) == fSimple(prices)
        f(prices, 10)
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