#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,utils
reload(sys)
sys.setdefaultencoding("utf-8")

class Solution:
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):
        path = path.strip().strip("/")
        paths = [p for p in path.split('/') if p and p != '.']
        results = []
        for p in paths:
            if p == '..':
                if results:
                    del results[-1]
            else:
                results.append(p)
        return "/" + '/'.join(results)

def sp(x):
    return Solution().simplifyPath(x)

def test():
    assert "//123//".strip("/") == '123'
    assert sp('///home///') == '/home'
    assert sp("/a/./b/../../c/") == '/c'
    assert sp("/home//foo/") == '/home/foo'
    assert sp('/..') == '/'

def main(args):
    
    pass

if __name__ == '__main__':
    main(sys.argv[1:])