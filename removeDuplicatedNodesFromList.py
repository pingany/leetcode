#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random
from random import randint
from LeetCodeUtils import *
   
def solve(node):
    if not node:
        return node
    head = ListNode(0)
    head.next = node

    prev = head
    node = head.next
    removeNode = False
    while node.next:
        if node.next.val == node.val:
            # remove node.next
            node.next = node.next.next
            removeNode = True
        else:
            if removeNode:
                nodeNext = node.next
                # remove node
                prev.next = nodeNext
                node = nodeNext
            else:
                prev = node
                node = node.next
            removeNode = False
    if removeNode:
        # remove node
        prev.next = node.next
    return head.next

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        return solve(head)
        
def solveSimple(list):
    count = collections.defaultdict(lambda:0)
    for x in list:
        count[x] +=1
    results = []
    for x in list:
        if count[x] > 1:
            pass
        else:
            results.append(x)
    return results

def sp(list1, list2):
    assert list2 == nodesToList(solve(listToNodes(list1)))
    pass
def test():
    sp([], [])
    sp([1], [1])
    sp([1,1,2], [2])
    sp([1,2], [1,2])
    sp([1,2], [1,2])
    sp([1,2,2,3], [1,3])
    sp([1,2,2,2], [1])
    sp([1,3,2,2,2], [1,3])
    sp([1,1,2,2,2], [])

    for x in xrange(1,100):
        list = [randint(0, 100) for i in range(x)]
        list.sort()
        sp(list, solveSimple(list))
        pass
    pass