#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2017-10-30 13:39:46;  @author: joinpython.com
'''

import re
print re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')

print re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')


data0="aaathethethe aatheaa"
data1="thethethe aatheaa"
data2="oooo"

print "介绍：match search findall："
m1 = re.match(r'the', data1) 
# print m1.group()
m2 = re.search(r'the', data0)

print "group 用法："
a = "123abc456"
print re.search("([0-9]*)([a-z]*)([0-9]*)",a).start()
print re.search("([0-9]*)([a-z]*)([0-9]*)",a).end()
print re.search("([0-9]*)([a-z]*)([0-9]*)",a).span()
print re.search("([0-9]*)([a-z]*)([0-9]*)",a).group()   #123abc456,返回整体
print re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(0)   #123abc456,返回整体
print re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(1)   #123
print re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(2)   #abc
print re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(3)   #456

print "贪婪和非贪婪匹配区别："
#贪婪
print re.findall(r'(the)+', data1)
#非贪婪
print re.findall(r'(the)+?', data1)

#贪婪
print re.findall(r'o+', data2)
#非贪婪
print re.findall(r'o+?', data2)

print "多行匹配："

data4="aaathethethez aatheaaz\naxxxz athez"
print re.findall(r'aaz.axx', data4)
print re.findall(r'aaz.axx', data4, re.S)
print re.findall(r'^a[a-z]+z', data4)
print re.findall(r'^a[a-z]+z', data4,re.M)


