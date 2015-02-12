#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random,heapq
from random import randint
from LeetCodeUtils import *
   
class PriorityQueue:  
    def __init__(self):  
        self._queue = []  
  
    def push(self, item):  
        heapq.heappush(self._queue, item)  
  
    def pop(self):  
        return heapq.heappop(self._queue) 

    def top(self):
        return self._queue[0]

    def remove(self, item):
        indexOfItem = self._queue.index(item)
        if indexOfItem < 0 :
            return False
        self._queue[indexOfItem] = self._queue[-1]
        self._queue.pop()
        if indexOfItem < len(self._queue):
            heapq._siftup(self._queue, indexOfItem)
        return True

    def verifyIsHeap(self):
        t = self._queue[:]
        heapq.heapify(t)
        assert t == self._queue

    def empty(self):
        return len(self._queue) == 0

    def __repr__(self):
        return "PriorityQueue:"+str(self._queue)
        pass

class MinStackSlow:
    def __init__(self):
        self.a = []
        self.q = PriorityQueue()
        pass
    # @param x, an integer
    # @return an integer
    def push(self, x):
        self.a.append(x)
        self.q.push(x)
        return x

    # @return nothing
    def pop(self):
        x = self.a.pop()
        removed = self.q.remove(x)
        assert removed

    # @return an integer
    def top(self):
        return self.a[-1]

    # @return an integer
    def getMin(self):
        return self.q.top()

# refer to http://leetcode.com/2010/11/stack-that-supports-push-pop-and-getmin.html
class MinStack:
    def __init__(self):
        self.a = []
        self.m = [] #MinStack
        pass
    # @param x, an integer
    # @return an integer
    def push(self, x):
        self.a.append(x)
        if not self.m or x <= self.m[-1]:
            self.m.append(x)
        return x

    # @return nothing
    def pop(self):
        x = self.a.pop()
        assert self.m[-1] <= x
        if self.m[-1] == x:
            self.m.pop()

    # @return an integer
    def top(self):
        return self.a[-1]

    # @return an integer
    def getMin(self):
        return self.m[-1]

def test():
    a= MinStack()
    a.push(1)
    a.push(2)

    assert a.getMin() == 1
    assert a.top() == 2
    assert a.a == [1, 2]
    a.pop()
    assert a.a == [1]

    assert 1 == a.top()
    a.pop()

    a= MinStack()
    for i in range(1, 1000):
        a.push(randint(1, 100000))
    for i in range(500):
        a.pop()
        # a.q.verifyIsHeap()
        assert a.getMin() == min(a.a)

def testPush():
    a = MinStack()
    for i in range(1, 100000):
        a.push(randint(1, 100))
def testPop():
    a = MinStack()
    for i in range(1, 100000):
        a.push(randint(1, 100))
    for i in range(1000):
        a.pop()
    pass