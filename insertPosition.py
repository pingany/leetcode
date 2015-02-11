#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,bisect
reload(sys)
sys.setdefaultencoding("utf-8")

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        a = A
        l = 0
        h = len(a)-1
        while l <= h:
            m = (l+h)/2
            if a[m] < target:
                l = m+1
            else:
                h = m-1
        return l


def sp(a, target, result):
    assert Solution().searchInsert(a, target) == result

from random import randint
def test():
    sp([], 1, 0)
    sp([], 0, 0)
    sp([1], 0, 0)
    sp([1], 1, 0)
    sp([1], 2, 1)

    sp([1, 2], 0, 0)
    sp([1, 2], 1, 0)
    sp([1, 2], 2, 1)

    for i in range(1000):
        a = range(randint(0, 100))
        target = randint(-1, 103)
        result = bisect.bisect_left(a, target)
        sp(a, target, result)

    for i in range(1000):
        a = sorted([randint(0, 2) for x in range(5)])
        target = randint(-1, 103)
        result = bisect.bisect_left(a, target)
        sp(a, target, result)


def searchInsertRight(A, target):
    a = A
    l = 0
    h = len(a)-1
    while l <= h:
        m = (l+h)/2
        if a[m] <= target:
            l = m+1
        else:
            h = m-1
    return l

def testRight():
    for i in range(1000):
        a = sorted([randint(0, 2) for x in range(500)])
        target = randint(-1, 103)
        result = bisect.bisect_right(a, target)
        assert searchInsertRight(a, target) == result

def main(args):
    
    pass

if __name__ == '__main__':
    main(sys.argv[1:])