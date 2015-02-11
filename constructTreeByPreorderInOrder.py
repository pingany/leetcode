#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,bisect
reload(sys)
sys.setdefaultencoding("utf-8")


# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node
    def buildTree(self, preorder, inorder):
        return self.buildTree2(preorder, 0, len(preorder), inorder, 0, len(inorder))

    def buildTree2(self, preorder, plo, phi, inorder, ilo, ihi):
        if plo >= phi:
            return None
        x = preorder[plo]
        root = TreeNode(x)
        index = ilo
        while index < ihi:
            if inorder[index] == x:
                break
            index += 1
        assert index < ihi
        i = index - ilo
        root.left = self.buildTree2(preorder, plo+1, plo+i+1, inorder, ilo, ilo+i)
        root.right = self.buildTree2(preorder, plo+i+1, phi, inorder, ilo+i+1, ihi)
        return root

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

from random import randint

class RandomTree():
    def __init__(self):
        self.val = 0

    def nextVal(self):
        self.val += 1
        return self.val

    def createTree(self):
        if self.val > 3:
            return None
        root = randint(0, 1) and TreeNode(self.nextVal()) or None
        if root:
            root.left = self.createTree()
            root.right = self.createTree()
        return root

def randomTest():
    tree = RandomTree().createTree()
    preorder = preOrderOut(tree, [])
    inorder = inOrderOut(tree, [])

    outTree = Solution().buildTree(preorder, inorder)
    assert preorder == preOrderOut(outTree, [])
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

    tree.left = TreeNode(2)
    assert treeEquals(Solution().buildTree([1, 2], [2, 1]), tree)
    tree.left.left = TreeNode(3)
    tree.left.left.left = TreeNode(4)
    assert [1, 2, 3, 4] == preOrderOut(tree, [])
    assert [4, 3, 2, 1] == inOrderOut(tree, [])

    assert treeEquals(Solution().buildTree([1, 2, 3, 4], [4, 3, 2, 1]), tree)


def test2():
    for i in range(100):
        randomTest()
def main(args):
    
    pass

if __name__ == '__main__':
    main(sys.argv[1:])