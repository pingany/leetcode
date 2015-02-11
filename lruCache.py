#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,utils
reload(sys)
sys.setdefaultencoding("utf-8")


class PriorityQueue:  
    def __init__(self):  
        self._queue = []  
  
    def put(self, item, priority):  
        heapq.heappush(self._queue, (-priority, item))  
  
    def get(self):  
        return heapq.heappop(self._queue)[-1]  

    def remove(self, item):
        self._queue[i] = self._queue[-1]
        self._queue.pop()
        heapq._siftup(self._queue, i)

    def empty(self):
        return len(self._queue) == 0

class Item(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value

class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.capacity = capacity
        self.map = {}
        self.queue = PriorityQueue()
        self.count = 0

    # @return an integer
    def get(self, key):
        if key not in self.map:
            return -1
        item = self.map[key]
        self.priorityUp(item)
        return item

    def priorityUp(self, item):
        self.queue.remove(item)
        self.count = self.count + 1
        self.queue.put(item, self.count)
        pass
    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key not in self.map and len(self.map) >= self.capacity:
            item = self.queue.get()
            del self.map[item.key]
        self.map[key] = item = Item(key, value)
        self.priorityUp(item)


def main(args):
    
    pass

if __name__ == '__main__':
    main(sys.argv[1:])