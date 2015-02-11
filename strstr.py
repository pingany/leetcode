#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob
reload(sys)
sys.setdefaultencoding("utf-8")

class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return an integer
    def strStr(self, haystack, needle):
        i = 0
        l = len(haystack) - len(needle)
        while i <= l:
            if haystack.startswith(needle, i):
                return i
            i = i + 1
        return -1

def sp(s, p, result):
    assert Solution().strStr(s, p) == result

def test():
    sp("", "", 0)
    sp("1", "", 0)
    sp("1", "2", -1)
    sp("1222", "2", 1)
    sp("1222", "1", 0)
    sp("1222", "122", 0)
    sp("1222", "222", 1)
    sp("1222", "2222", -1)

def main(args):
    
    pass

if __name__ == '__main__':
    main(sys.argv[1:])