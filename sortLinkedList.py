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
    prev = node
    while n > 0 and node:
        n -= 1
        prev = node
        node = node.next
    return node, prev

def merge(node1, node2, l):
    head = ListNode(0)
    prev = head
    l1 = l
    l2 = l
    while (node1 and l1) or (node2 and l2):
        condition1 = node1 and l1
        condition2 = node2 and l2
        if condition1 and ((not condition2) or node1.val < node2.val):
            x = node1
            node1 = node1.next
            l1 -= 1
            assert l1 >= 0
        else:
            assert node2
            x = node2
            node2 = node2.next
            l2 -= 1
            assert l2 >= 0
        prev.next = x
        prev = x
    return head.next

def sortList(node):
    head = ListNode(0)
    head.next = node
    len = listLen(node)
    l = 1
    while l < len:
        prev = head
        print "len ", l
        while node:
            next, _ = listTraverse(node, l)
            prev.next = merge(node, next, l)

            print listLen(prev.next)
            node, prev = listTraverse(prev.next, l*2)
        l *= 2
    return head.next

def assertMergeOK(l1, l2, l3, length=1000):
    assert l3 == nodesToList(merge(listToNodes(l1), listToNodes(l2), length),
        min(length, len(l1))+min(length, len(l2)))

def assertSortOK(list):
    node = listToNodes(list)
    node2 = sortList(node)
    assert nodesToList(node2) == sorted(list)

def test():
    node1 = listToNodes([1, 2])
    node2 = listToNodes([2, 3])
    node3 = merge(node1, node2, 10)
    assert [1, 2, 2, 3] == nodesToList(node3)

    assertMergeOK([], [], [])
    assertMergeOK([], [1], [1])
    assertMergeOK([1], [], [1])
    assertMergeOK([1], [1], [1, 1])
    assertMergeOK([1], [2], [1, 2])
    assertMergeOK([2], [1], [1, 2])

    assertMergeOK([2], [1], [], 0)
    assertMergeOK([2,3], [1,1], [1, 2], 1)
    assertMergeOK([2,3], [1,1], [1, 1, 2, 3], 2)

    assert merge(None, None, 100) == None
    node = ListNode(1)
    assert merge(node, None, 100) == node
    assert merge(None, node, 100) == node

    assertSortOK([1, 2])
    assertSortOK([1])
    assertSortOK([])
    assertSortOK([1, 2, 1])
def test2():
    assertSortOK([2, 1])
    pass