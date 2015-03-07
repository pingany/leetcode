#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random
from random import randint
from LeetCodeUtils import *
   
def fSimple(prices):
    n = len(prices)
    ff = [0]*(n+1)
    ff[n] = 0
    for i in range(n-2, -1, -1):
        for j in range(i+1, n+1):
            ff[i] = max(ff[i], ff[j] + prices[j-1]-prices[i])
    return ff[0]

def f(prices):
    n = len(prices)
    i = 1
    profit = 0
    while i < n:
        while i < n and prices[i] <= prices[i-1]:
            i += 1
            pass
        if i >= n:
            break
        low = prices[i-1]
        while i < n and prices[i] >= prices[i-1]:
            i += 1
            pass
        up = prices[i-1]
        assert up >= low
        profit += up - low
    return profit

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

def test2():
    prices = json.load(open("stock2.in"))
    print len(prices)
    f(prices)
    pass