#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,math,collections
reload(sys)
sys.setdefaultencoding("utf-8")
# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# list should be reversed
def buildTreeStructure(num):
    if not num:
        return None
    root = TreeNode(0)
    num = num - 1
    queue = collections.deque([root])
    q = collections.deque([])
    while len(queue) > 0 and num:
        q.clear()
        for node in queue:
            if num:
                node.left = TreeNode(0)
                num = num - 1
                q.append(node.left)
            if num:
                node.right = TreeNode(0)
                num = num - 1
                q.append(node.right)
        # swap t queue
        t = queue
        queue = q
        q = t
    return root


def middleOrderIn(root, iterable):
    if not root:
        return
    if root.left:
        middleOrderIn(root.left, iterable)
    root.val = iterable.next()
    if root.right:
        middleOrderIn(root.right, iterable)

def buildTree(iterable):
    root = buildTreeStructure(len(iterable))
    middleOrderIn(root, iterable)
    return root

class ListNodeIter():
    def __init__(self, node):
        self.node = node
        l = 0
        while node:
            node = node.next
            l = l +1
        self.length = l

    def next(self):
        self.length = self.length - 1
        node = self.node
        self.node = node.next
        return node.val
    def hasNext(self):
        return self.node != None
    def __len__(self):
        return self.length
        
class Solution:
    # @param head, a list node
    # @return a tree node
    def sortedListToBST(self, head):
        return buildTree(ListNodeIter(head))

def middleOrderOut(root, results):
    if not root:
        return results
    if root.left:
        middleOrderOut(root.left, results)
    results.append(root.val)
    if root.right:
        middleOrderOut(root.right, results)
    return results
# def buildTreeLevel(root, level):
#     if not root:
#         return
#     root.level = level
#     buildTreeLevel(root.left, level+1)
#     buildTreeLevel(root.right, level+1)

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

def assertTreeOk(root, level, maxDepth):
    if root:
        assert level <= maxDepth
    if level < maxDepth:
        assert root
    if not root:
        return
    if level >= maxDepth:
        return
    assertTreeOk(root.left, level+1, maxDepth)
    assertTreeOk(root.right, level+1, maxDepth)

def doTest(l):
    tree = Solution().sortedListToBST(listToNodes(l))
    assert middleOrderOut(tree, results=[]) == l

    # buildTreeLevel(tree, 1)
    maxDepth = int(math.ceil(math.log(len(l)+1, 2)))
    assertTreeOk(tree, 1, maxDepth);

def test():
    doTest(list("4251637"))
    doTest(list(""))
    doTest(list("0"))
    doTest(list("1"))
    doTest(list("12"))
    doTest(list("123"))
    doTest(list("4251637fadsfasdf"))
    doTest(list("4251637fadsfasdf1413241321432"))
    doTest(list("4251637fadsfasdf1413241321432fdfadsfasdfsdfa"))
    doTest(list("4251637fadsfasdf1413241321432fadsfqerw314132fadsfsdfqwr13"))
    doTest(list("31432vdvr13fsdfqewr13r1r131434123"))
    doTest(list("12312"))
    doTest([-1,0,1,2])

def main(args):
    
    pass

if __name__ == '__main__':
    main(sys.argv[1:])