#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random
from random import randint
from LeetCodeUtils import *
   
def insert(node, nodeToInsert, tempHead):
    head = tempHead
    head.next = node
    node = head
    while node.next and node.next.val <= nodeToInsert.val:
        node = node.next
    nodeToInsert.next = node.next
    node.next = nodeToInsert
    return head.next

def reverseNodes(node):
    if not node:
        return node
    head = ListNode(0)
    while node:
        next= node.next
        node.next = head.next
        head.next = node
        node = next
    return head.next

def insertionSort(node):
    sortedList = ListNode(0)
    prev = None
    while node is not None:
        next = node.next
        p = sortedList
        if prev is not None and prev.val <= node.val:
            p = prev
        
        while p.next and p.next.val <= node.val:
            p = p.next
        node.next = p.next
        p.next = node

        prev = node
        node = next
    return sortedList.next

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def insertionSortList(self, head):
        return insertionSort(head)
def sp(a):
    assert nodesToList(insertionSort(listToNodes(a))) == sorted(a)

def testR():
    for i in range(1, 100):
        a = [randint(1, 100) for x in range(i)]
        sp(a)

def testBig():
    sp(range(5000))

def testBig2():
    sp(range(5000, 0, -1))
    pass
def test():
    assert insertionSort(None) == None

    node = ListNode(1)
    assert insertionSort(node) == node

    sp([]) == []
    sp([1]) == [1]
    sp([2, 1]) == [2, 1]
    sp([1, 1]) == [1, 1]

    pass

if __name__ == '__main__':
    testBig2()