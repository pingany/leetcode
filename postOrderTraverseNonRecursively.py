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
        
def postorderNonRecursive(node):
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
            toReverse.appendleft(node.right)
        if node.left:
            toReverse.appendleft(node.left)
    return results

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        return postorderNonRecursive(root)

def test():
    assert postorderNonRecursive(None) == []
    assert postorderNonRecursive(TreeNode(1)) == [1]

    node = TreeNode(1, 
                TreeNode(2, 
                    TreeNode(4, 
                        TreeNode(6,
                            None,
                            TreeNode(7))),
                    TreeNode(5)),
                TreeNode(3,
                    TreeNode(10)))
    assert [7, 6, 4, 5, 2, 10, 3, 1] == postOrderOut(node, [])
    assert [7, 6, 4, 5, 2, 10, 3, 1] == postorderNonRecursive(node)
def test2():
    for i in range(100):
        node = RandomTree(10).createTree()
        assert postorderNonRecursive(node) == postOrderOut(node, [])
    pass