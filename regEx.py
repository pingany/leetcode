#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random
from random import randint
from LeetCodeUtils import *
   
def devideRegex(p):
    r = []
    i = 0
    n = len(p)
    while i < n:
        if i + 1 < n and p[i+1] =='*':
            r.append(p[i:i+2])
            i += 2
        else:
            r.append(p[i])
            i += 1
    return r

def matches2(s, p):
    p = devideRegex(p)
    def matchRegex(s, i, p, j):
        if j == len(p):
            return i == len(s)
        if i == len(s):
            return all([len(x) == 2 for x in p[j:]])
        assert i < len(s)
        assert j < len(p)                
        if s[i] == p[j][0] or p[j][0] == '.':
            if len(p[j]) > 1:
                assert p[j][1] == '*'
                return matchRegex(s, i+1, p, j) or matchRegex(s, i, p, j+1)
            else:
                return matchRegex(s, i+1, p, j+1)
        elif len(p[j]) > 1:
            return matchRegex(s, i, p, j+1)
        return False
    return matchRegex(s, 0, p, 0)

def array2(row, col, initValue=None):
    return [[initValue for x in range(col)] for x in range(row)] 

def matchAny(x):
    return len(x) > 1

def matches(s, p):
    p = devideRegex(p)
    m = len(s)
    n = len(p)
    f = array2(m+1, n+1)
    for i in range(m, -1, -1):
        for j in range(n, -1, -1):
            if j == n:
                x = (i == m)
            elif i == m:
                x = f[i][j+1] if matchAny(p[j]) else False
            elif s[i] == p[j][0] or p[j][0] == '.':
                if matchAny(p[j]):
                    x = f[i+1][j] or f[i][j+1]
                else:
                    x = f[i+1][j+1]
            elif matchAny(p[j]):
                x = f[i][j+1]
            else:
                x = False
            f[i][j] = x
    return f[0][0]

class Solution:
    # @param s, a string
    # @param p, a string
    # @return a boolean
    def isMatch(self, s, p):
        return matches(s, p)
        
def sp(*a):
    assert solve(*a[:-1]) == a[-1]
    pass
def test():
    assert devideRegex("a") == ['a']
    assert devideRegex("abc") == list('abc')
    assert devideRegex("b*") == ['b*']
    assert devideRegex("b*.*") == ['b*', '.*']
    assert devideRegex("ab*c.*d") == ['a', 'b*', 'c', '.*', 'd']

    assert matches('aa', 'a') == False
    assert matches('a', 'a') == True
    assert matches('a', '') == False
    assert matches('', '.*') == True
    assert matches('', 'a*') == True
    assert matches('a', 'a*') == True
    assert matches('aa', 'a*') == True
    assert matches('aaa', 'a*') == True
    assert matches('aaa', '.*') == True
    assert matches('aa', 'aa') == True
    assert matches('aaa', 'aa') == False
    assert matches('abc', '.*') == True
    assert matches('aab', 'c*a*b*') == True
    assert matches('b', 'c*a*b*') == True
    assert matches('', 'c*a*b*') == True
    assert matches('','') == True
    pass