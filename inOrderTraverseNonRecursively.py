#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random
from random import randint
from LeetCodeUtils import *
   
class HashWrapper():
    def __init__(self, object):
        self.object = object
    def __hash__(self):
        return id(self.object)
    def __eq__(self, a):
        return self.object == a.object 
        
def inorderNonRecursive(node):
    if not node:
        return []
    toReverse = collections.deque([node])
    results = []
    traversed = set()
    while len(toReverse) > 0:
        node = toReverse[0]

        if (not node.left and not node.right):
            results.append(toReverse.popleft().val)
            continue
        elif HashWrapper(node) in traversed:
            results.append(toReverse.popleft().val)
            traversed.remove(HashWrapper(node))
            continue
        else:
            traversed.add(HashWrapper(node))
        if node.right:
            # toReverse.insert(1, node.right)
            toReverse.popleft()
            toReverse.appendleft(node.right)
            toReverse.appendleft(node)
        if node.left:
            toReverse.appendleft(node.left)
    return results

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def inorderTraversal(self, root):
        return inorderNonRecursive(root)

def test():
    for i in range(100):
        node = RandomTree(10).createTree()
        assert inorderNonRecursive(node) == inOrderOut(node, [])
    pass
