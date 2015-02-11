#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,utils
reload(sys)
sys.setdefaultencoding("utf-8")

letters = [
    "abc",
    "def",
    "ghi",
    "jkl",
    "mno",
    "pqrs",
    "tuv",
    "wxyz",
]

def letter(x):
    return letters[int(x) - 2]

class Solution:
    def __init__(self):
        self.digits = None
        self.letters = None
        pass
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        r = []
        self.digits = digits
        self.letters = [None]*len(digits)
        self.f(0, r)
        return r

    def f(self, i, results):
        if i == len(self.digits):
            results.append("".join(self.letters[:]))
            return
        for a in letter(self.digits[i]):
            self.letters[i] = a
            self.f(i+1, results)

        
def sp(digits, list):
    assert Solution().letterCombinations(digits) == list

def test():
    sp("", [""])
    sp("2", ["a", "b", "c"])
    sp("23", ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])
    pass

if __name__ == '__main__':
    main(sys.argv[1:])