#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random
from random import randint
from LeetCodeUtils import *

def array2(row, col, initValue=None):
    return [[initValue for x in range(col)] for x in range(row)] 

def updateResult(i, j, result):
    k = j - i +1
    if k > result[0]:
        result[0], result[1], result[2] = k, i, j
    pass
def solve(s):
    n = len(s)
    if not n:
        return ""
    result = [1, 0, 0]
    isPalindorm = array2(n, n, None)
    for i in range(n-1, -1, -1):
        isPalindorm[i][i] = True
        if i+1 < n:
            ok = isPalindorm[i][i+1] = s[i] == s[i+1]
            if ok:
                updateResult(i, i+1, result)
        for j in range(i+2, n):
            ok = isPalindorm[i][j] = s[i] == s[j] and isPalindorm[i+1][j-1]
            if ok:
                updateResult(i, j, result)
    return s[result[1]:result[2]+1]
    pass
class Solution:
    # @return a string
    def longestPalindrome(self, s):
        return solve(s)
def sp(*a):
    assert solve(*a[:-1]) == a[-1]
    pass
def test():
    sp("", "")
    sp("123", "1")
    sp("122", "22")
    sp("121", "121")
    sp("1212121", "1212121")
    sp("xabcbad", "abcba")
    pass

def testBig():
    solve("aaaabbbbbbbbbbccccccccccddddddddddeeeeeeeeeeffffffffffgggggggggghhhhhhhhhhiiiiiiiiiijjjjjjjjjjkkkkkkkkkkllllllllllmmmmmmmmmmnnnnnnnnnnooooooooooppppppppppqqqqqqqqqqrrrrrrrrrrssssssssssttttttttttuuuuuuuuuuvvvvvvvvvvwwwwwwwwwwxxxxxxxxxxyyyyyyyyyyzzzzzzzzzzyyyyyyyyyyxxxxxxxxxxwwwwwwwwwwvvvvvvvvvvuuuuuuuuuuttttttttttssssssssssrrrrrrrrrrqqqqqqqqqqppppppppppoooooooooonnnnnnnnnnmmmmmmmmmmllllllllllkkkkkkkkkkjjjjjjjjjjiiiiiiiiiihhhhhhhhhhggggggggggffffffffffeeeeeeeeeeddddddddddccccccccccbbbbbbbbbbaaaaaaaabbbbbbbbbbccccccccccddddddddddeeeeeeeeeeffffffffffgggggggggghhhhhhhhhhiiiiiiiiiijjjjjjjjjjkkkkkkkkkkllllllllllmmmmmmmmmmnnnnnnnnnnooooooooooppppppppppqqqqqqqqqqrrrrrrrrrrssssssssssttttttttttuuuuuuuuuuvvvvvvvvvvwwwwwwwwwwxxxxxxxxxxyyyyyyyyyyzzzzzzzzzzyyyyyyyyyyxxxxxxxxxxwwwwwwwwwwvvvvvvvvvvuuuuuuuuuuttttttttttssssssssssrrrrrrrrrrqqqqqqqqqqppppppppppoooooooooonnnnnnnnnnmmmmmmmmmmllllllllllkkkkkkkkkkjjjjjjjjjjiiiiiiiiiihhhhhhhhhhggggggggggffffffffffeeeeeeeeeeddddddddddccccccccccbbbbbbbbbbaaaa")
    # assert "1"*1000 == solve("1"*1000)
    pass