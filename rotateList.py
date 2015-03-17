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

def solve(node, k):
    if not node:
        return node
    n = listLen(node)
    k %= n

    head = ListNode(0)
    head.next = node

    node2Prev = listTraverse(head, n-k)
    node2 = node2Prev.next
    if not node2:
        return node
    node2Prev.next = None

    tail = node2
    while tail.next:
        tail = tail.next
    tail.next = head.next

    return node2

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):
        return solve(head, k)
import rotateArray
def solveList(list, k):
    list = list[:]
    rotateArray.Solution().rotate(list, k)
    return list
def sp(*a):
    assert solve(*a[:-1]) == a[-1]
    pass
def test():

    sp(None, 5, None)
    node = ListNode(0)
    sp(node, 0, node)
    sp(node, 1, node)
    sp(node, 2, node)

    node = ListNode(0, ListNode(1))
    sp(node, 1, node.next)

    for i in range(1000):
        x = range(i)
        k = randint(0, i*10)
        assert nodesToList(solve(listToNodes(x), k)) == solveList(x, k)
    pass