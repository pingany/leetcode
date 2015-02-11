

#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob
reload(sys)
sys.setdefaultencoding("utf-8")

class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        prev = None
        results = []
        for n in range(1, numRows+1):
            r = [1]
            for i in range(0, n-2):
                r.append(prev[i]+prev[i+1])
            if n > 1:
                r.append(1)
            prev = r
            results.append(r)
        return results


def sp(numRows, results):
    assert results == Solution().generate(numRows)

def test():
    sp(0, [])
    sp(1, [[1]])
    sp(2, [
     [1],
    [1,1]])
    sp(5, [
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
])

def main(args):
    
    pass

if __name__ == '__main__':
    main(sys.argv[1:])