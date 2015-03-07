#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random
from random import randint
from LeetCodeUtils import *
   
# head is a useless node
def insertList(head, nodeToInsert):
    p = head
    while p.next and p.next.val <= nodeToInsert.val:
        p = p.next
    nodeToInsert.next = p.next
    p.next = nodeToInsert
    pass

def mergeLists(list1, list2):
    head = ListNode(0)
    head.next = list1

    p = list2
    insertPosition = head
    while p:
        next = p.next
        insertList(insertPosition, p)
        insertPosition = p
        p = next
        pass
    return head.next

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        return mergeLists(l1, l2)
def sp(list1, list2, results):
    assert results == mergeLists(list1, list2)
    pass
def test():
    node = ListNode(1)
    sp(None, node, node)
    sp(node, None, node)
    node2 = ListNode(2)

    sp(node, node2, node)
    sp(node2, node, node)
    pass

def testR():
    for i in range(1, 100):
        l1 = [randint(0, 100) for x in range(i)]
        l2 = [randint(0, 100) for x in range(i)]
        l1.sort()
        l2.sort()
        r = mergeLists(listToNodes(l1), listToNodes(l2))
        assert sorted(l1+l2) == nodesToList(r)
    pass