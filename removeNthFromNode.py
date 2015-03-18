#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random
from random import randint
from LeetCodeUtils import *

def solve(node, n):
    if not node or n <= 0:
        return node
    n -= 1
    head = ListNode(0)
    head.next = node

    candidatePrev = head
    c = n
    while c:
        node = node.next
        c -= 1
        
    while node.next:
        node = node.next
        candidatePrev = candidatePrev.next
    # delete
    candidatePrev.next = candidatePrev.next.next
    return head.next

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        return solve(head, n)
def sp(*a):
    assert solve(*a[:-1]) == a[-1]
    pass
def test():
    node = ListNode(1)
    sp(node, 1, None)

    node = ListNode(1, ListNode(2))
    sp(node, 2, node.next)
    pass