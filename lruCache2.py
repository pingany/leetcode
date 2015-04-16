#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random
from random import randint
from LeetCodeUtils import *

class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = None
        self.prev = None
        if next:
            self.insertBehind(next)

    def remove(self):
        assert self.prev
        prev = self.prev
        next = self.next

        prev.next = next
        if next:
            next.prev = prev

    # insert node after this, return self
    def insertBehind(self, node):
        assert node
        nodeNext = self.next

        self.next = node
        node.next = nodeNext

        if nodeNext:
            nodeNext.prev = node
        node.prev = self
        return self

    def __repr__(self):
        return "ListNode(%s, %s)" % (str(self.val), repr(self.next))
        pass

class Queue:
    def __init__(self, list=None):
        self.head = ListNode(0)
        self.tail = self.head

        if list:
            for v in reversed(list):
                self.pushFront(ListNode(v))
        pass

    def pushFront(self, node):
        assert isinstance(node, ListNode)
        self.head.insertBehind(node)
        if self.head == self.tail:
            self.tail = node
        pass

    def popBack(self):
        assert self.tail
        node = self.tail
        self.remove(self.tail)
        return node
        pass

    def remove(self, node):
        assert node
        if node == self.tail:
            self.tail = node.prev
        if node.prev: # node may not in this queue
            node.remove()
        pass

    def checkPointers(self):
        l = []
        if self.tail:
            node = self.tail
            while node != self.head:
                l.append(node.val)
                node = node.prev
                pass
        l.reverse()
        assert l == nodesToList(self.head.next)
        pass

    def toList(self):
        # self.checkPointers()
        return nodesToList(self.head.next)


class NodeValue:
    def __init__(self, k, v):
        self.key = k
        self.value = v
        pass

class LRUCache:
    # @param capacity, an integer
    def __init__(self, capacity):
        self.queue = Queue()
        self.map = {}
        self.capacity = capacity

    # @return an integer
    def get(self, key):
        if key not in self.map:
            return -1
        node = self.map[key]
        self.queue.remove(node)
        self.queue.pushFront(node)
        return node.val.value    

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key not in self.map:
            if len(self.map) >= self.capacity:
                node=self.queue.popBack()
                del self.map[node.val.key]
            node = ListNode(NodeValue(key, value))
            self.map[key] = node
        else:
            node = self.map[key]
            node.val.value = value
        self.queue.remove(node)
        self.queue.pushFront(node)

    def queueValues(self):
        return [v.value for v in self.queue.toList()]
        pass

def sp(*a):
    assert solve(*a[:-1]) == a[-1]
    pass
def testQueue():
    q = Queue([2,3,4])
    node2 = ListNode(2)
    node1 = ListNode(1)
    q.pushFront(node2)
    q.pushFront(node1)
    q.popBack()
    q.checkPointers()
    assert [1,2,2,3] == q.toList()

    q.pushFront(ListNode(0))
    q.popBack()
    assert [0,1,2,2] == q.toList()

    q.remove(node1)
    assert [0,2,2] == q.toList()
    q.remove(node2)
    assert [0,2] == q.toList()
    pass

def test():
    c = LRUCache(2)
    assert -1 == c.get(1)

    c.set(1,1)
    assert c.get(1)
    assert [1] == c.queueValues()

    c.set(2,2)
    assert [2, 1] == c.queueValues()
    assert c.get(1)
    assert [1, 2] == c.queueValues()
    c.set(2,2)
    assert [2, 1] == c.queueValues()

    assert -1 == c.get(3)
    c.set(3, 3)
    assert [3, 2] == c.queueValues()
    assert -1 == c.get(1)

    c = LRUCache(10)
    for i in range(100):
        c.set(i,i)
    assert range(99, 90-1,-1) == c.queueValues()
    for i in range(99, 90-1,-1):
        c.set(i, 1)
    assert [1]*10 == c.queueValues()
    pass

if __name__ == '__main__':
    test()