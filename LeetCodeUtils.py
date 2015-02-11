#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def listToNodes(l):
    if not l:
        return None
    head = node = ListNode(0)
    for x in l:
        n = ListNode(x)
        node.next = n
        node = n
    return head.next
def nodesToList(node):
    l = []
    while node:
        l.append(node.val)
        node = node.next
    return l
def unqiue(list):
    return sorted(set(list))

def testThis():
    def assertOk(list):
        assert list == nodesToList(listToNodes(list))
    assertOk([])
    assertOk([1])
    assertOk(["1"])
    assertOk([1, 2])
    assertOk([1, 2,3 ,4])
    pass

