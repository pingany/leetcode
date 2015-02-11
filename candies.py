#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob
reload(sys)
sys.setdefaultencoding("utf-8")

def candies(ratings):
    if not ratings:
        return 0
    n = len(ratings)
    c = [1]*n
    i = 1
    while i < n:
        prev = i-1
        while i < n and ratings[i] == ratings[i-1]:
            i += 1

        if i - prev > 1:
            for j in range(prev+1, i-1):
                assert c[j] == 1

        prev = i-1
        while i < n and ratings[i] < ratings[i-1]:
            i+=1
        if i - prev > 1:
            x = 1
            for j in range(i-1, prev-1, -1):
                c[j] = max(c[j], x)
                x += 1

        prev = i-1
        while i < n and ratings[i] > ratings[i-1]:
            i+=1

        if i - prev > 1:
            x = 1
            for j in range(prev, i, 1):
                c[j] = max(c[j], x)
                x += 1
    return sum(c),c

class Solution:
    # @param ratings, a list of integer
    # @return an integer
    def candy(self, ratings):
        return candies(ratings)[0]

def sp(ratings, result):
    assert Solution().candy(ratings)[0] == result
    pass

def test():
    sp([], 0)
    sp([1], 1)
    sp([2], 1)
    sp([1, 2], 3)
    sp([1, 2, 1], 4)
    sp([0, 2, 0], 4)
    sp([-1, 2, -1], 4)
    sp([1,2,3,-1], 7)
    sp([1,2,2], 4)
    pass

from random import randint
def test2():
    for i in range(1, 100):
        ratings = [randint(0, i) for x in range(i)]
        s, c = candies(ratings)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                assert c[i] > c[i-1]
            elif ratings[i] < ratings[i-1]:
                assert c[i] < c[i-1]
def main(args):
    
    pass

if __name__ == '__main__':
    main(sys.argv[1:])