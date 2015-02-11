#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob
reload(sys)
sys.setdefaultencoding("utf-8")

# Definition for a point
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

def isZero(x):
    return abs(x) < 1e-9
    pass
class Angle:
    def __init__(self, p1, p2):
        dx = float(p1.x - p2.x)
        dy = float(p1.y - p2.y)
        self.vertical = isZero(dx)
        if self.vertical:
            self.a = 0
            self.b = p1.x
        else:
            self.a = dy/dx
            self.b = p1.y - self.a*p1.x
        self.a = round(self.a, 8)
        self.b = round(self.b, 8)

    def __hash__(self):
        return hash((self.vertical, self.a, self.b))

    def __eq__(self, angle2):
        return self.vertical == angle2.vertical and isZero(self.a - angle2.a) and isZero(self.b - angle2.b)

    def __repr__(self):
        return str((self.vertical, self.a, self.b))
        pass

class Solution:
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
        n = len(points)
        if n < 2:
            return n
        angleMap = {}
        for i in range(0, n-1):
            for j in range(i+1, n):
                a = Angle(points[i], points[j])
                if a not in angleMap:
                    angleMap[a] = set([i, j])
                else:
                    s = angleMap[a]
                    s.add(i)
                    s.add(j)
        if angleMap:
            # print angleMap
            numbers = [len(x) for x in angleMap.values()]
            return max(numbers)
        return 0
        
def sp(points, res):
    assert Solution().maxPoints(points) ==res

def test():
    sp([], 0)
    sp([Point(0, 0)], 1)
    sp([Point(0, 0), Point(1, 1)], 2)
    sp([Point(0, 0), Point(0, 1)], 2)
    sp([Point(0, 0), Point(1, 0)], 2)
    sp([Point(0, 0), Point(1, 1), Point(2, 2)], 3)
    sp([Point(0, 0), Point(1, 1), Point(2, 2.1)], 2)

    sp([Point(0, x) for x in range(0, 100)], 100)
    sp([Point(x, 0) for x in range(0, 100)], 100)
    sp([Point(x, x) for x in range(0, 100)], 100)

def test2():
    sp([Point(x, x) for x in range(0, 200)] + [Point(x, 0) for x in range(1, 100)], 200)
def main(args):
    
    pass

if __name__ == '__main__':
    main(sys.argv[1:])