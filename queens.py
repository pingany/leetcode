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
    results = []
    def canPut(row, col):
        for i in range(row):
            j = pick[i]
            if j == col:
                return False
            if abs(i-row) == abs(j-col):
                return False
        return True
        pass
    def putFrom(row):
        if row == n:
            results.append([getDotRow(col) for col in pick])
            return
        for col in range(n):
            if canPut(row, col):
                pick[row]=col
                putFrom(row+1)
        pass
    putFrom(0)
    return results
class Solution:
    # @return a list of lists of string
    def solveNQueens(self, n):
        return solve(n)

def sp(*a):
    assert solve(*a[:-1]) == a[-1]
    pass
def test():
    sp(1, [['Q']])
    sp(4, [
 [".Q..",  # Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  # Solution 2
  "Q...",
  "...Q",
  ".Q.."]
])
    pass