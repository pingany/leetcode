#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random
from random import randint
from LeetCodeUtils import *
   
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class HashWrapper():
    def __init__(self, object):
        self.object = object
    def __hash__(self):
        return id(self.object)
    def __eq__(self, a):
        return self.object == a.object 
        
def copy(head):
    oldNewMap = {}

    # newHead, with a head node
    newHead = RandomListNode(1)
    prev = newHead

    oldNode = head
    while oldNode:
        prev.next = RandomListNode(oldNode.label)
        prev.next.random = oldNode.random
        oldNewMap[HashWrapper(oldNode)] = prev.next
        prev = prev.next
        oldNode = oldNode.next
    
    node = newHead.next
    while node:
        if node.random:
            node.random = oldNewMap[HashWrapper(node.random)]
        node = node.next
    return newHead.next

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        return copy(head)

def randomNodesToList(node):
    l = []
    while node:
        l.append((node.label, node.random.label if node.random else None))
        node = node.next
        pass
    return l

def createRandomNodes(list):
    if not list:
        return None
    nodes = [RandomListNode(v) for v in list]
    for i in range(0, len(nodes)-1):
        nodes[i].next = nodes[i+1]
    for i in range(0, len(nodes)):
        nodes[i].random = nodes[randint(0, len(nodes)-1)] if randint(0,1) == 0 else None
    return nodes[0]

def sp(*a):
    assert copy(*a[:-1]) == a[-1]
    pass
def test():

    node = createRandomNodes([1,2,3])
    list1 = randomNodesToList(node)
    list2 = randomNodesToList(copy(node))
    assert list1 == list2

    for i in range(100):
        list = [randint(1, 100) for x in range(i)]
        node = createRandomNodes(list)
        list1 = randomNodesToList(node)
        list2 = randomNodesToList(copy(node))
        assert list1 == list2
    pass