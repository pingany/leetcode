#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random
from random import randint
from LeetCodeUtils import *
   
def solve(n):

    def getDotRow(col):
        r = ['.']*n
        r[col] = 'Q'
        return "".join(r)       

    pick = [None]*n
    results = [0]
    def canPut(row, col):
        for i in range(row):
            j = pick[i]
            if j == col:
                return False
            if abs(i-row) == abs(j-col):
                return False
        return True
        pass
    def f(row):
        if row == n:
            results[0] += 1
            return
        for col in range(n):
            if canPut(row, col):
                pick[row]=col
                f(row+1)
        pass
    f(0)
    return results[0]
class Solution:
    # @return an integer
    def totalNQueens(self, n):
        return solve(n)

def sp(*a):
    assert solve(*a[:-1]) == a[-1]
    pass

def test():
    sp(1, 1)
    sp(4, 2)
    pass