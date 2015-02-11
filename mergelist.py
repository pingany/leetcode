#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class PriorityQueue:  
    def __init__(self):  
        self._queue = []  
  
    def put(self, item, priority):  
        heapq.heappush(self._queue, (-priority, item))  
  
    def get(self):  
        return heapq.heappop(self._queue)[-1]  

    def empty(self):
        return len(self._queue) == 0

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

class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        q = PriorityQueue()
        for node in lists:
            if node:
                q.put(node, -node.val)

        r = []
        while not q.empty():
            node = q.get()
            r.append(node.val)
            node = node.next
            if node:
                q.put(node, -node.val)
        return listToNodes(r)


class ListSolution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        lists = [x[:] for x in lists if x];
        r = []
        while lists:
            firsts = [x[0] for x in lists]
            first = min(firsts)
            r.append(first)
            i = 0;
            for l in lists:
                if l[0] == first:
                    del l[0]
                    if not l:
                        del lists[i]
                    break
                i = i + 1
        return r

def resolve(lists):
    node = Solution().mergeKLists([listToNodes(l) for l in lists])
    return nodesToList(node)

def testBasic():
    assert resolve([[1, 2], [4, 5]]) == [1, 2, 4,5] 
    assert resolve([[1, 2], [4]]) == [1, 2, 4] 
    assert resolve([[1], [4]]) == [1, 4] 
    assert resolve([[1], [1, 2]]) == [1, 1, 2] 
    assert resolve([[1, 1], [1, 2]]) == [1, 1, 1, 2] 
    assert resolve([[], [1, 2]]) == [1, 2] 
    assert resolve([[], []]) == [] 

def test1():
    lists = eval(open("in.txt").read())
    print >> sys.stderr, (len(lists))
    resolve(lists)

def main(args):
    test1()
    pass

if __name__ == '__main__':
    main(sys.argv[1:])