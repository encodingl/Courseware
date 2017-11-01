#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2017-10-26 16:40:44;  @author: joinpython.com
'''

class menu:
    def __init__(self,name,**materials):
        self.name="m1"
        self.materials=materials        
class buyer:
    def __init__(self,name):
        self.name=name
    def buy(self,menu):
        pass    
class assitant_chef: 
    def __init__(self,name):
        self.name=name
    def prepare(self,menu):
        pass    
class chef:
    def __init__(self,name):
        self.name=name
    def prepare(self,menu):
        pass
class waiter:
    def __init__(self,name):
        self.name=name
    def serve(self,menu,desknum):
        pass
if __name__ == "__main__":
    m1 = menu(name="m1",materrials={"tomato":1,"egg":1})
    buyer01=buyer(name="ZhangShan")
    buyer01.buy(menu="m1")
    assitant_chef01=assitant_chef(name="LiShan")
    assitant_chef01.prepare(menu="m1")
    chef01=assitant_chef(name="HuangShan")
    chef01.prepare(menu="m1")
    waiter01=waiter(name="ZhuShan")
    waiter01.serve(menu="m1",desknum=1)
    