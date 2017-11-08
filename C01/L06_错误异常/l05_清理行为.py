#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
Create on 2017-11-08 17:06:56;@author:joinpython.com
'''
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print "division by zero!"
    else:
        print "result is", result
    finally:
        print "executing finally clause"

divide(2, 0)

