#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random
from random import randint
from LeetCodeUtils import *
   
def solve(node):
    head = ListNode(0)
    head.next = node
    prev = head

    while node:
        if not node.next:
            return head.next
        next = node.next
        next2 = node.next.next

        prev.next = next
        next.next = node
        node.next = next2

        prev = node
        node = next2
        pass
    return head.next


class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        return solve(head)
def sp(*a):
    assert solve(*a[:-1]) == a[-1]
    pass

def assertList(list):
    node = listToNodes(list)
    node2 = solve(node)
    list2 = nodesToList(node2)

    for i in range(0, len(list), 2):
        if i + 1 < len(list):
            list[i], list[i+1] = list[i+1], list[i]

    assert list == list2
def test():
    sp(None, None)

    node = ListNode(1)
    sp(node, node)

    node.next = ListNode(2)
    node = solve(node)
    assert nodesToList(node) == [2, 1]

    assertList([])
    assertList([1])
    assertList([1,2])
    for i in range(1, 100):
        a = [randint(1, 100) for x in range(i)]
        assertList(a)
    pass