#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob
reload(sys)
sys.setdefaultencoding("utf-8")

def reverseWords(s):
    l = [x for x in s.strip().split(' ') if x]
    l.reverse()
    return " ".join(l)

class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        return reverseWords(s)

def sp(x, y):
    assert Solution().reverseWords(x) == y
def test():
    sp("", "")
    sp("1", "1")
    sp("1 2", "2 1")
    sp("  1    2    ", "2 1")
    sp("  11   2    ", "2 11")
    pass
if __name__ == '__main__':
    main(sys.argv[1:])