#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random
from random import randint
from LeetCodeUtils import *
   
def solve(node1, m, n):
    head = ListNode(0)
    head.next = node1
    prev = head

    i = 0
    while i < m:
        prev = prev.next
        i += 1
        pass

    n -= m
    nodeToInsertPrev = prev.next
    while n > 0:
        n -= 1

        node = nodeToInsertPrev.next
        nodeToInsertPrev.next = node.next

        node.next = prev.next
        prev.next = node

        pass
    return head.next
    pass

class Solution:
    # @param head, a ListNode
    # @param m, an integer
    # @param n, an integer
    # @return a ListNode
    def reverseBetween(self, head, m, n):
        return solve(head, m-1, n-1)
def doTest(l, m, n):
    assert 0 <=m and m <= n and n <= len(l)-1
    result = nodesToList(solve(listToNodes(l), m, n))

    expected = l[:m] + list(reversed(l[m:n+1])) + l[n+1:]
    assert expected == result
    pass
def testS():
    doTest([1, 2, 3], 0, 2)
    pass
def test():
    doTest([1], 0, 0)
    doTest([1, 2], 0, 0)
    doTest([1, 2, 3], 0, 1)
    doTest([1, 2, 3], 1, 2)
    for i in range(1, 100):
        list = [randint(1, 100) for x in range(i)]
        for m in range(i):
            for n in range(m, i):
                doTest(list, m, n)
    pass