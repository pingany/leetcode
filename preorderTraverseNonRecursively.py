#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random
from random import randint
from LeetCodeUtils import *
   
def preorderNonRecursive(node):
    if not node:
        return []
    toReverse = collections.deque([node])
    results = []
    while len(toReverse) > 0:
        node = toReverse.popleft()
        results.append(node.val)
        if node.right:
            toReverse.appendleft(node.right)
        if node.left:
            toReverse.appendleft(node.left)
    return results

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        return preorderNonRecursive(root)

def test():
    assert preorderNonRecursive(None) == []
    assert preorderNonRecursive(TreeNode(1)) == [1]
    for i in range(100):
        node = RandomTree(10).createTree()
        assert preorderNonRecursive(node) == preOrderOut(node, [])
    pass