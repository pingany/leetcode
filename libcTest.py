#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os,re,sys,commands,glob,json,collections,random
from random import randint
from LeetCodeUtils import *
   

from ctypes import *

libc = CDLL("libc.so.6")

def test():
    libc.printf("test printf %d %.02f %s", 1, 1.0, "str")
    pass