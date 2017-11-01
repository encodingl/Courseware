#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2017-10-28 18:39:20;  @author: joinpython.com
'''



import sys
print '没有重定向之前打印信息'   

#重定向分界线
                                       
saveout = sys.stdout                                     
fsock = open('/tmp/out.log', 'w')                             
sys.stdout = fsock                                       
print '已经进行重定向了' 

#还原重定向配置
sys.stdout = saveout 
print "重定向已还原"                                    
fsock.close()  



