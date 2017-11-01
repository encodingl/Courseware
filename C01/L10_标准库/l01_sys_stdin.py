#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2017-10-28 18:28:11;  @author: joinpython.com
'''
import sys



print "Please enter your name: "
name = sys.stdin.readline()
print name


# cat a.py
import sys
sys.stdout.write("123456\n")
sys.stdout.flush()
# cat b.py
import sys
print sys.stdin.readlines()
 
# python a.py | python b.py
['123456\n']
