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


def f(a, b):
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
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        return f(headA, headB)

def sp(x, y, z):
    assert f(x, y) == z
def test():
    sp(None, None, None)
    sp(ListNode(0), None, None)
    sp(None, ListNode(0), None)
    sp(ListNode(0), ListNode(0), None)

    common = ListNode(0, ListNode(1))
    a = ListNode(0, ListNode(1, ListNode(2, ListNode(3, common))))
    b = ListNode(0, ListNode(1, ListNode(2, ListNode(3, common))))
    sp(a, b, common)
    sp(b, a, common)

    b = ListNode(0, common)
    sp(a, b, common)
    sp(b, a, common)

    b = common
    sp(a, b, common)
    sp(b, a, common)
    pass