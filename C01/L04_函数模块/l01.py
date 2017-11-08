#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
Create on 2017-11-07 21:41:06;@author:joinpython.com
'''

def ask_ok(retries=4, complaint='Yes or no, please!'):
    while True:
        ok = raw_input()
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise IOError('refusenik user')
        print complaint
if __name__ == "__main__":      
    ask_ok()

