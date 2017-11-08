#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
Create on 2017-11-08 13:37:12;@author:joinpython.com
'''

func=lambda x:x+1
print(func(1))
#2
print(func(2))
#3
func2=lambda x,y:x+y
print func2(1,2)
#以上lambda等同于以下函数
def dfunc(x):
    return(x+1)
