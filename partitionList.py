#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random
from random import randint
from LeetCodeUtils import *

def removeNext(node):
    assert node.next
    node.next = node.next.next
    pass

def insertNode(prev, node):
    assert prev and node
    node.next = prev.next
    prev.next = node
    pass
   
def solve(node, val):
    if not node:
        return node
    head = ListNode(0)
    head.next = node

    bigPrev = bigHead = ListNode(0)
    nodePrev = head

    while node:
        next = node.next
        if node.val >= val:
            removeNext(nodePrev)
            insertNode(bigPrev, node)
            bigPrev = node
        else:
            nodePrev = node
        node = next
        pass
    nodePrev.next = bigHead.next
    return head.next
    pass

class Solution:
    # @param head, a ListNode
    # @param x, an integer
    # @return a ListNode
    def partition(self, head, x):
        return solve(head, x)

def partitionList(list, val):
    small = []
    big = []
    for x in list:
        if x < val:
            small.append(x)
        else:
            big.append(x)
    return small + big
    pass
def sp(list, val, expected):
    assert partitionList(list, val) == expected
    list2 = nodesToList(solve(listToNodes(list), val))
    assert list2 == expected
    pass
def test():
    sp([], 0, [])
    sp([], 1, [])
    sp([1], 1, [1])
    sp([0], 0, [0])
    sp([0], 1, [0])
    sp([0,0,1], 1, [0,0,1])
    sp([5,4,3,2,1], 3, [2,1,5, 4, 3])
    pass
def testR():
    for i in range(100):
        list = [randint(1, 100) for x in range(i)]
        sp(list, 50, partitionList(list, 50))
    pass