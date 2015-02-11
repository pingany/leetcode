#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,utils
reload(sys)
sys.setdefaultencoding("utf-8")

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        if not head:
            return False
        p1 = p2 = head
        while True:
            p1 = p1.next
            p2 = self.move2(p2)
            if not p1 or not p2:
                return False
            if p1 == p2:
                return True
        assert False

    @staticmethod
    def move2(node):
        node = node.next
        if node:
            node = node.next
        return node
def listToNodes(l):
    if not l:
        return None
    head = node = ListNode(0)
    nodes = {}
    for x in l:
        if x in nodes:
            n = nodes[x]
        else:
            n = ListNode(x)
            nodes[x] = n
        node.next = n
        node = n
    return head.next
def nodesToList(node):
    l = []
    while node:
        l.append(node.val)
        node = node.next
    return l

def assertOk(list, hasCycle):
    assert Solution().hasCycle(listToNodes(list)) == hasCycle

def test():
    assertOk([], False)
    assertOk([1], False)
    assertOk([1,2], False)
    assertOk([1,1], True)
    assertOk([1,2,2], True)
    assertOk([1,2,3,3], True)
    assertOk([1,2,3,4,3], True)
    assertOk([1,2,3,4,2], True)
    assertOk([1,2,3,4,1], True)
    assertOk([1,2,1], True)
    assertOk([1,2,1,2,1,2], True)
    pass

def main(args):
    
    pass

if __name__ == '__main__':
    main(sys.argv[1:])