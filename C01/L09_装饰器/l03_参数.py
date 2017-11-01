#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2017-10-28 17:20:13;  @author: joinpython.com
'''

import logging
def use_logging(level):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if level == "warn":
                logging.warn("%s is running" % func.__name__)
            return func(*args)
        return wrapper
    return decorator


@use_logging(level="warn")
def foo(name='foo'):
    print("i am %s" % name)
foo()
