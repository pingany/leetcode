#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random
from random import randint
from LeetCodeUtils import *
   

def listLen(node):
    l = 0
    while node:
        l += 1
        node = node.next
    return l

def listTraverse(node, n):
    while n > 0 and node:
        n -= 1
        node = node.next
    return node

def getIntersectionNode(a, b):
    l1 = listLen(a)
    l2 = listLen(b)
    if not l1 or not l2:
        return None
    if l1 > l2:
        a = listTraverse(a, l1-l2)
    elif l1 < l2:
        b = listTraverse(b, l2-l1)

    while a:
        if a == b:
            return a
        a = a.next
        b = b.next

    assert not a
    assert not b
    return None

class Solution:
    def detectCycle(self, head):
        if not head:
            return None

        p1 = p2 = head
        nodeInCycle = None
        while True:
            p1 = p1.next
            p2 = self.move2(p2)
            if not p1 or not p2:
                return None
            if p1 == p2:
                nodeInCycle = p1
                break
        assert nodeInCycle
        nodeInCycleNext = nodeInCycle.next
        nodeInCycle.next = None

        result = getIntersectionNode(head, nodeInCycleNext)
        nodeInCycle.next = nodeInCycleNext
        return result

    @staticmethod
    def move2(node):
        node = node.next
        if node:
            node = node.next
        return node

def solve(node):
    return Solution().detectCycle(node)
    pass
def sp(*a):
    assert solve(*a[:-1]) == a[-1]
    pass
def test():
    sp(None, None)

    node = ListNode(0)
    sp(node, None)

    node.next = node
    sp(node, node)

    head = ListNode(0, node)
    sp(head, node)

    head = ListNode(0, ListNode(0, ListNode(0, ListNode(0, node))))
    sp(head, node)

    head = ListNode(0, ListNode(0))
    head.next.next = head
    sp(head, head)
    pass