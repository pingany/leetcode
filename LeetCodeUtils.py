#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob
from collections import deque, defaultdict

from random import randint

INT_MAX = (1 << 30)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

    def __repr__(self):
        return "ListNode(%s, %s)" % (str(self.val), repr(self.next))
        pass

def listToNodes(l):
    if not l:
        return None
    head = node = ListNode(0)
    for x in l:
        n = ListNode(x)
        node.next = n
        node = n
    return head.next
def nodesToList(node, maxLen=INT_MAX):
    l = []
    while node and maxLen:
        maxLen -= 1
        l.append(node.val)
        node = node.next
    return l

def listLen(node):
    l = 0
    while node:
        l += 1
        node = node.next
    return l

def listTraverse(node, n):
    while n > 0 and node:
        n -= 1
        node = node.next
    return node


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

def unqiue(list):
    return sorted(set(list))


def treeEquals(n1, n2):
    if n1 == n2:
        return True
    if not n1 or not n2:
        return False
    if n1.val == n2.val:
        return treeEquals(n1.left, n2.left) and treeEquals(n1.right, n1.right)
    return False

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

    def __repr__(self):
        return "Tree(%d, %s, %s)" % (self.val, self.left, self.right)
        pass

def inOrderOut(root, results):
    if not root:
        return results
    if root.left:
        inOrderOut(root.left, results)
    results.append(root.val)
    if root.right:
        inOrderOut(root.right, results)
    return results

def preOrderOut(root, results):
    if not root:
        return results
    results.append(root.val)
    if root.left:
        preOrderOut(root.left, results)
    if root.right:
        preOrderOut(root.right, results)
    return results

def postOrderOut(root, results):
    if not root:
        return results
    if root.left:
        postOrderOut(root.left, results)
    if root.right:
        postOrderOut(root.right, results)
    results.append(root.val)
    return results

class RandomTree():
    def __init__(self, maxNodes=10):
        self.val = 0
        self.maxNodes = maxNodes

    def nextVal(self):
        self.val += 1
        return self.val

    def createTree(self):
        if self.val > self.maxNodes:
            return None
        root = randint(0, 1) and TreeNode(self.nextVal()) or None
        if root:
            root.left = self.createTree()
            root.right = self.createTree()
        return root

def itToList(iterable):
    l =[]
    while iterable.hasNext():
        l.append(iterable.next())
    return l

def dictTree():
    return defaultdict(dictTree)

def compare(x, y):
    if x > y:
        return 1
    elif x < y:
        return -1
    else:
        return 0
def testThis():
    def assertOk(list):
        assert list == nodesToList(listToNodes(list))
    assertOk([])
    assertOk([1])
    assertOk(["1"])
    assertOk([1, 2])
    assertOk([1, 2,3 ,4])

    assert(listLen(None)) == 0
    assert(listLen(ListNode(0))) == 1
    assert(listLen(listToNodes([])) == 0)
    assert(listLen(listToNodes([1])) == 1)
    assert(listLen(listToNodes([1,2])) == 2)

    assert listTraverse(None, 0) == None
    assert listTraverse(None, 10) == None

    node = ListNode(0)
    assert listTraverse(node, 0) == node
    assert listTraverse(node, 1) == node.next

    node = ListNode(0, ListNode(1, ListNode(2)))
    assert listTraverse(node, 0) == node
    assert listTraverse(node, 1) == node.next
    assert listTraverse(node, 2) != None
    assert listTraverse(node, 3) == None
    assert listTraverse(node, 4) == None
    assert listTraverse(node, 100) == None

    assert(listLen(listTraverse(None, 0))) == 0
    assert(listLen(listTraverse(None, 1))) == 0

    pass

class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
        
class HashWrapper():
    def __init__(self, object):
        self.object = object
    def __hash__(self):
        return id(self.object)
    def __eq__(self, a):
        return self.object == a.object 
        

def array2(row, col, initValue=None):
    return [[initValue for x in range(col)] for x in range(row)] 


def removeNext(node):
    assert node.next
    node.next = node.next.next
    pass

def insertNode(prev, node):
    assert prev and node
    node.next = prev.next
    prev.next = node
    pass
   