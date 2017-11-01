#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2017-10-28 16:52:03;  @author: joinpython.com
'''

#简单的装饰器
import logging
def use_logging(func):
    def wrapper(*args, **kwargs):
        logging.warn("%s is running" % func.__name__)
        return func(*args, **kwargs)
    return wrapper
def bar():
    print('i am bar')
bar = use_logging(bar)
bar()

print "xxxxxx"

