#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob
reload(sys)
sys.setdefaultencoding("utf-8")

def isPalindrom(s, i, size):
    j = i + size - 1
    while i < j:
        if s[i] != s[j]:
            return False
        i = i +1 
        j = j -1
    return True

def partition(s, i, results, current=[]):
    if i == len(s):
        results.append(current[:])
        return
    for size in range(1, len(s)-i+1):
        if isPalindrom(s, i, size):
            current.append(s[i:i+size])
            partition(s, i+size, results, current)
            current.pop()
        else:
            continue

class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        if not s:
            return []
        results = []
        partition(s, 0, results, [])
        return results         

def sp(s, list):
    assert sorted(Solution().partition(s)) == sorted(list)

def test():
    sp("1", [["1"]])
    sp("11", [["1", "1"],["11"]])
    sp("12", [["1", "2"]])
    sp("aab", [
    ["aa","b"],
    ["a","a","b"]
  ])
    sp("efe", [["e","f","e"],["efe"]])

def test2():
    sp("", [])

def main(args):
    
    pass

if __name__ == '__main__':
    main(sys.argv[1:])