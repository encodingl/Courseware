#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
Create on 2017-11-07 21:41:06;@author:joinpython.com
'''

def fsum(a,b):
    "数字相加和相乘"
    print "a:%s,b:%s" % (a,b)
    c=a+b
    d=a*b
    return c,d;

if __name__ == "__main__":      
    rc=fsum(1,2)
    print rc

