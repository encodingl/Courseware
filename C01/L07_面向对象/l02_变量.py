#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2017-10-26 17:02:53;  @author: joinpython.com
'''

class Person:
    num_count = 0 # 所有的实例都共享此变量，即不单独为每个实例分配 
    def __init__(self, name):
        self.name = name  #对象变量
        self.__class__.num_count += 1 
        self.__age="I am pri_age"
        self.age="I am not pri_age"
        print name,self.__class__.num_count
    
    def sayHi(self):
        print 'Hello, my name is', self.name
    def __del__(self):
        self.__class__.num_count -= 1 
        print "del",self.name,self.__class__.num_count
        
        
        

        
        
if __name__ == "__main__":
    csk1 = Person('sk1')
#     csk2 = Person('sk2')
#     csk3 = Person('sk3')
    print "over"
    
    p = Person('skipper')
#     p.sayHi()
    print p.name
    print p.age
    print p.__age
    