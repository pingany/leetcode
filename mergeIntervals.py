#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,utils
reload(sys)
sys.setdefaultencoding("utf-8")

# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    @classmethod
    def fromList(cls, a, b):
        return Interval(a, b)

    def toList(self):
        return [self.start, self.end]

    def __eq__(self, a):
        return self.start == a.start and self.end == a.end 

def last(interval):
    return interval.end

def overlap(a, b):
    assert a.start <= b.start
    return last(a) >= b.start

def merge(a, b):
    assert a.start <= b.start
    a.end = max(a.end, b.end)
    return a

class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval
    def merge(self, intervals):
        intervals = sorted(intervals, cmp=lambda x,y:x.start-y.start)
        merged = []
        for val in intervals:
            needAppend = True
            if merged:
                if overlap(merged[-1], val):
                    merge(merged[-1], val)
                    needAppend = False
            if needAppend:
                merged.append(val)
        return merged

def assertMergeOk(lists, resultLists):
    intervals = [Interval.fromList(*list) for list in lists]
    merged = Solution().merge(intervals)
    assert [interval.toList() for interval in merged] == resultLists

def test():
    assert overlap(Interval.fromList(1, 2), Interval.fromList(1, 1))
    assert overlap(Interval.fromList(1, 2), Interval.fromList(1, 2))
    assert overlap(Interval.fromList(1, 2), Interval.fromList(1, 3))
    assert not overlap(Interval.fromList(1, 2), Interval.fromList(3, 3))
    assert not overlap(Interval.fromList(1, 2), Interval.fromList(3, 3))
    assert merge(Interval.fromList(1, 2), Interval.fromList(1, 2)) == Interval.fromList(1, 2)
    assert merge(Interval.fromList(1, 2), Interval.fromList(1, 3)) == Interval.fromList(1, 3)

    assertMergeOk([[1, 2], [2, 6], [8, 10], [15, 15]], [[1, 6], [8, 10], [15, 15]])
    assertMergeOk([[1, 2], [1, 6], [8, 10], [15, 15]], [[1, 6], [8, 10], [15, 15]])
    assertMergeOk([[1, 2], [0, 6], [8, 10], [15, 15]], [[0, 6], [8, 10], [15, 15]])
    assertMergeOk([[1, 2], [0, 6], [1, 3], [2, 4], [8, 10], [15, 15]], [[0, 6], [8, 10], [15, 15]])
    assertMergeOk([[1, 2], [15, 15], [2, 6], [8, 10]], [[1, 6], [8, 10], [15, 15]])

    assertMergeOk([[1,4],[4,5]], [[1, 5]])
def main(args):
    
    pass

if __name__ == '__main__':
    main(sys.argv[1:])