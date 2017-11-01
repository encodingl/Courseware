#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2017-10-30 11:23:27;  @author: joinpython.com
'''

import sys


# raise Exception, '未重定向之前抛出异常'
fsock = open('/tmp/l10error.log', 'w')               
sys.stderr = fsock                           
raise Exception, '重定向之后抛出异常'