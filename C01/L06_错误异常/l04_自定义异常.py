#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
Create on 2017-11-08 17:01:39;@author:joinpython.com
'''
class MyError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)
    
    
# try:
#     raise MyError(2*2)
# except MyError as e:
#     print 'My exception occurred, value:', e.value

raise MyError("oops!")