#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random
from random import randint
from LeetCodeUtils import *

class Solution:
    # @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node
    def buildTree(self, inorder, postorder):
        return self.buildTree2(postorder, 0, len(postorder), inorder, 0, len(inorder))

    def buildTree2(self, postorder, plo, phi, inorder, ilo, ihi):
        if plo >= phi:
            return None
        x = postorder[phi-1]
        root = TreeNode(x)
        # find x from inorder[ilo:ihi]
        index = ilo
        while index < ihi:
            if inorder[index] == x:
                break
            index += 1
        assert index < ihi

        i = index - ilo
        root.left = self.buildTree2(postorder, plo, plo+i, inorder, ilo, ilo+i)
        root.right = self.buildTree2(postorder, plo+i, phi-1, inorder, ilo+i+1, ihi)
        return root

def randomTest():
    tree = RandomTree().createTree()
    postorder = postOrderOut(tree, [])
    inorder = inOrderOut(tree, [])

    outTree = Solution().buildTree(inorder, postorder)
    assert postorder == postOrderOut(outTree, [])
    assert inorder == inOrderOut(outTree, [])
    pass

def treeEquals(n1, n2):
    if n1 == n2:
        return True
    if not n1 or not n2:
        return False
    if n1.val == n2.val:
        return treeEquals(n1.left, n2.left) and treeEquals(n1.right, n1.right)
    return False

def test():
    tree = None
    assert treeEquals(Solution().buildTree([], []), tree)

    tree = TreeNode(1)
    assert treeEquals(Solution().buildTree([1], [1]), tree)


def test2():
    for i in range(100):
        randomTest()
def main(args):
    
    pass

if __name__ == '__main__':
    main(sys.argv[1:])