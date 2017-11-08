#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
Create on 2017-11-07 21:17:50;@author:joinpython.com
'''

for letter in 'Python':     # 第一个实例
   print '当前字母 :', letter
 
fruits = ['banana', 'apple',  'mango']
for fruit in fruits:        # 第二个实例
   print '当前水果 :', fruit
 
print "Good bye!"

# 输出 2 到 100 简的质数
prime = []
for a in range(1,10):
    print a
for num in range(2,100):  # 迭代 2 到 100 之间的数字
   for i in range(2,num): # 根据因子迭代
      if num%i == 0:      # 确定第一个因子
         break            # 跳出当前循环
   else:                  # 循环的 else 部分
      prime.append(num)
print prime

