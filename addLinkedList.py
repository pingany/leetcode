#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random
from random import randint
from LeetCodeUtils import *
   
def f(a, b):
    c = 0
    head = ListNode(0)
    prev = head
    while a or b:
        if a:
            c += a.val
            a = a.next
        if b:
            c += b.val
            b = b.next
        prev.next = ListNode(c%10)
        prev = prev.next
        c /= 10
    if c:
        prev.next = ListNode(c)
    return head.next

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        return f(l1, l2)

def intToNodes(x):
    l = list(str(x))
    l.reverse()
    l = [int(x) for x in l]
    return listToNodes(l)

def nodesToInt(node):
    l = nodesToList(node)
    l = [str(x) for x in l]
    l.reverse()
    return int("".join(l))

def assertAdd(x, y):
    z = x + y
    assert nodesToInt(f(intToNodes(x), intToNodes(y))) == z

def test():
    assert f(None, None) == None
    node = ListNode(1)
    assert f(None, node).val == 1
    assert f(node, None).val == 1

    assert nodesToList(intToNodes(123)) == [3, 2, 1]
    assert nodesToInt(listToNodes([3, 2, 1])) == 123
    for i in range(1000):
        x = randint(0, 1000)
        y = randint(0, 1000)
        assertAdd(x, y)
    pass