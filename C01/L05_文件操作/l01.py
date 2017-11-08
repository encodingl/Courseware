#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
Create on 2017-11-08 14:08:48;@author:joinpython.com
'''

fo = open("foo.txt",'a+')

print "文件名: ", fo.name
print "是否已关闭 : ", fo.closed
print "访问模式 : ", fo.mode


# fo.write( "www.joinpython.com!\nVery good site!\n");
str1=fo.read(12)
print "读取的字符串是 : ", str1

print "*"*40
for line in fo.readlines():
    print line.strip()
    
fo.close() # 关闭打开的文件


with open("foo.txt","a+") as f:
    f.write("i have been opened by withopen")






