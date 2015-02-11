#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob
reload(sys)
sys.setdefaultencoding("utf-8")

class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        a = A
        if not a:
            return 0
        l = len(a)
        k = 1
        i = 1
        while i < l:
            if a[i] != a[i-1]:
                a[k] = a[i]
                k += 1
            i += 1
        return k

def sp(a, results):
    k = Solution().removeDuplicates(a)
    assert len(a) == k
    assert results == a[:k]

def test():
    sp([], [])
    sp([1], [1])
    sp([1, 1], [1])
    sp([1, 2], [1, 2])
    sp([1, 1, 2], [1, 2])
    sp([1, 1, 1], [1])
    sp([1, 2, 1], [1, 2, 1])
    pass

def main(args):
    
    pass

if __name__ == '__main__':
    main(sys.argv[1:])