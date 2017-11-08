#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2017-11-07 00:27:15;  @author: joinpython.com
'''

dict = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
B = dict
print dict
dict['Alice'] = 8222; # update existing entry
print dict
del dict['Alice']; # 删除键是'Name'的条目b
print dict
# dict.clear();     # 清空词典所有条目
# print dict
D={'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
print D.keys()            #返回字典键的列表  
print D.values()          #以列表的形式返回字典中的值，返回值的列表中可包含重复元素  
print B.keys()
print D.get("Alice1", 0)       #同dict[key]，多了个没有则返回缺省值，0。[]没有则抛异常  
print D.has_key("Alice1")      #有该键返回TRUE，否则FALSE  

print D.items()           #将所有的字典项以列表方式返回，这些列表中的每一项都来自于(键,值),但是项在返回时并没有特殊的顺序           


