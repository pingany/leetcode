#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random
from random import randint
from LeetCodeUtils import *
   
def listReverse(node):
    head = ListNode(0)
    while node:
        # save next
        next = node.next
        # insert node after head
        node.next = head.next
        head.next = node
        # go to next
        node = next
    return head.next

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
    return node,prev

def solve(node):
    n = listLen(node)
    if n <= 2:
        return node
    part1Len = (n+1)/2

    part2Start,part2StartPrev = listTraverse(node, part1Len)
    part2StartPrev.next = None

    part2Start = listReverse(part2Start)

    head = node
    node2 = part2Start
    while node2:
        nodeNext = node.next
        node2Next = node2.next

        # insert node2 after node
        node2.next = node.next
        node.next = node2

        node2 = node2Next
        node = nodeNext
    return head

class Solution:
    # @param head, a ListNode
    # @return nothing
    def reorderList(self, head):
        solve(head)

def solveList(list):
    n = len(list)
    part1Len = (n+1)/2
    list1 = list[:part1Len]
    list2 = list[part1Len:]
    list2.reverse()
    for i in range(len(list2)):
        list1.insert(i*2+1, list2[i])
    return list1

def sp(*a):
    assert solve(*a[:-1]) == a[-1]
    pass
def spList(list1, list2):
    assert list2 == nodesToList(solve(listToNodes(list1)))
    assert list2 == solveList(list1)
    pass

def test():
    sp(None, None)

    node = ListNode(0)
    sp(node, node)

    node = ListNode(0, ListNode(1))
    sp(node, node)

    spList([], [])
    spList([1], [1])
    spList([1,2], [1,2])
    spList([1,2,3], [1,3,2])
    spList([1,2,3,4], [1,4,2,3])

    for i in range(500):
        list = [randint(1, 10000) for x in range(i)]
        spList(list, solveList(list))
    pass