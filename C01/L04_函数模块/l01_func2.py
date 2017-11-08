#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
Create on 2017-11-08 13:29:24;@author:joinpython.com
'''

def cheeseshop(kind, *arguments, **keywords):
    print "-- Do you have any", kind, "?"
    print "-- I'm sorry, we're all out of", kind
    for arg in arguments:
        print arg
    print "-" * 40
    keys = sorted(keywords.keys())
    for kw in keys:
        print kw, ":", keywords[kw]
        
def test(x,**y):
    if y==0:
        x="suc"
    else:
        x="fai"
    print x,y 
        
if __name__ == "__main__":    
    test("b",y=0,y1=4,y2=5)
    print "*"*40

    cheeseshop("Limburger", "It's very runny, sir.",
               "It's really very, VERY runny, sir.",
               shopkeeper='Michael Palin',
               client="John Cleese",
               sketch="Cheese Shop Sketch")