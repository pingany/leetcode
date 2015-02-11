#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random
from random import randint
from LeetCodeUtils import *
class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):
        if not head:
            return head
        prev = head
        node = head.next
        while node:
            if prev and node.val == prev.val:
                prev.next = node.next
            else:
                prev = node
            node = node.next
        return head

def sp(list, result):
    node = Solution().deleteDuplicates(listToNodes(list))
    assert nodesToList(node) == result

def test():
    sp([], [])
    sp([1], [1])
    sp([1, 1], [1])
    sp([1, 1, 1], [1])
    sp([1, 1, 2], [1,2])
    sp([1, 1, 2, 2], [1,2])
    sp([1, 1, 2, 2, 3], [1,2, 3])
    for i in range(5, 100):
        l = [randint(1, 5) for x in range(1, i)]
        l = sorted(l)
        sp(l, unqiue(l))
    pass