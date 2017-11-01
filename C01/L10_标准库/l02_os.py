#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2017-10-28 17:55:06;  @author: joinpython.com
'''
import os

os.getcwd()      # Return the current working directory
os.chdir('/tmp')   # Change current working directory
os.system('mkdir today')   # Run the command mkdir in the system shell


#在使用一些像 os 这样的大型模块时内置的 dir() 和 help() 函数非常有用:
# dir(os)
# help(os)