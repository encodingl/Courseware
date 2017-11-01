#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2017-10-28 17:23:09;  @author: joinpython.com
'''
import logging
def use_logging(func):
    def wrapper(*args, **kwargs):
        logging.warn("%s is running" % func.__name__)
        return func(*args, **kwargs)
    return wrapper

#语法糖
@use_logging
def foo():
    print("i am foo")
    
foo()
