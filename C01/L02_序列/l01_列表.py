#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2017-11-02 09:58:50;  @author: joinpython.com
'''
list1 = ['physics', 'chemistry', 1997, 2000];
print list1
list2 = [1, 2, 3, 4, 5 ];
l2=list2
list2.remove(3)
list2=[11,12]
print l2
list2.append(7)
print l2
list3 = ["a", "b", "c", "d"];
list1.append("joinpython")
print list1
print "joinpython test listtttttttttttttttttttttt"
L=list1
print L
L.extend(list2)  #追加list，即合并list到L上 
print L 
L.sort()        #排序   ；L.reverse()     #倒序  ；list 操作符:,+,*，关键字del  
print L
print "joinpython test bbbbb"
print L[1:]       #片段操作符，用于子list的提取  
print [1,2]+[3,4] #为[1,2,3,4]。同extend()  
print [2]*4       #为[2,2,2,2]  
del L[1]    #删除指定下标的元素  ；del L[1:3]  #删除指定下标范围的元素  
print L


