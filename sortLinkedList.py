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

def listInsert(node, nodeToInsert, maxStep=(1<<30)):
    if maxStep <= 0 or not nodeToInsert:
        return node
    head = ListNode(0)
    head.next = node
    prev = head
    while maxStep > 0 and node and node.val <= nodeToInsert.val:
        prev = node
        node = node.next
        maxStep -= 1
    prev.next = nodeToInsert
    nodeToInsert.next = node
    return head.next

def merge(node1, node2, l):
    assert l > 0
    l1 = l
    l2 = l
    while l1 > 0 and node1:
        node1Next = node1.next
        node2 = listInsert(node2, node1, l2)
        l1 -= 1
        l2 += 1
        node1 = node1Next
    return node2

def sortList(node):
    head = ListNode(0)
    head.next = node
    len = listLen(node)
    l = 1
    while l < len:
        prev = head
        node = prev.next
        # assert len == listLen(node)
        while node:
            next, _ = listTraverse(node, l)
            prev.next = merge(node, next, l)
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

def testInsert():
    node = listToNodes([1, 2])
    node = listInsert(node, ListNode(3))
    assert [1, 2, 3] == nodesToList(node)

    node = listInsert(node, ListNode(0))
    assert [0, 1, 2, 3] == nodesToList(node)

    node = listInsert(node, ListNode(1.5))
    assert [0, 1, 1.5, 2, 3] == nodesToList(node)

    node = listInsert(node, ListNode(4), 0)
    assert [0, 1, 1.5, 2, 3] == nodesToList(node)

    node = listInsert(node, ListNode(4), 1)
    assert [0, 4, 1, 1.5, 2, 3] == nodesToList(node)

    node = listInsert(node, ListNode(-1), 1)
    assert [-1, 0, 4, 1, 1.5, 2, 3] == nodesToList(node)

    node = listToNodes([1, 2])
    assert [1, 2, 2] == nodesToList(listInsert(node, ListNode(2)))
    assert [1, 2, 2, 3] == nodesToList(listInsert(node, ListNode(3)))

    assert [] == nodesToList(listInsert(None, None))
    assert [1] == nodesToList(listInsert(ListNode(1), None))
    assert [1] == nodesToList(listInsert(None, ListNode(1)))

def testMerge():
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

    assertMergeOK([2,3], [1,1], [1, 2], 1)
    assertMergeOK([2,3], [1,1], [1, 1, 2, 3], 2)

    assertMergeOK([2,3], [1], [1, 2, 3], 1000)

    assert merge(None, None, 100) == None
    node = ListNode(1)
    assert merge(node, None, 100) == node
    assert merge(None, node, 100) == node

    node = listToNodes([2, 1])
    sortedNode = merge(node, node.next, 1)
    assert [1, 2] == nodesToList(sortedNode)

    node = listToNodes([2])
    sortedNode = merge(node, node.next, 1)
    assert [2] == nodesToList(sortedNode)

    node = listToNodes([2, 1, 0])
    sortedNode = merge(node, node.next, 1)
    assert [1, 2, 0] == nodesToList(sortedNode)

    assert None == merge(None, None, 100)
    assert None == merge(None, None, 1)

    node = ListNode(2)
    assert node == merge(None, node, 1)
    assert node.next == None
    assert node == merge(node, None, 1)
    assert node.next == None

    assert [2] == nodesToList(merge(ListNode(2, ListNode(1)), None,1))
    assert [1, 2] == nodesToList(merge(ListNode(2, ListNode(1)), None,2))
    assert [1, 2] == nodesToList(merge(ListNode(2, ListNode(1)), None,3))

    node = listToNodes([3, 4, 1, 5, 2])
    assert [1, 3, 4, 5, 2] == nodesToList(merge(node, listTraverse(node, 2)[0], 2))

    node = listToNodes([3, 4, 1, 5, 2])
    assert [1, 2, 3, 4, 5] == nodesToList(merge(node, listTraverse(node, 4)[0], 4))

def testTraverse():
    assert (None, None) == listTraverse(None, 0)
    assert (None, None) == listTraverse(None, 1)
    assert (None, None) == listTraverse(None, 100)

    node = ListNode(1)
    assert (node, node) == listTraverse(node, 0)
    assert (node.next, node) == listTraverse(node, 1)
    assert (node.next, node) == listTraverse(node, 1000)

    node = listToNodes([1, 2])
    assert (node.next, node) == listTraverse(node, 1)
    assert (node.next.next, node.next) == listTraverse(node, 2)
    assert (None, node.next) == listTraverse(node, 3)
    assert (None, node.next) == listTraverse(node, 1000)

def testSort():
    assertSortOK([2, 1])

    assertSortOK([1, 2])
    assertSortOK([1])
    assertSortOK([])
    assertSortOK([1, 2, 1])

    for i in range(100):
        assertSortOK([randint(1, 1000) for x in range(0, i)])

def testPerformance():
    assertSortOK([randint(1, 1000) for x in range(1000)])
    pass