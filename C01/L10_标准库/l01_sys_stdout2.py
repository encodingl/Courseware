#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2017-10-30 11:16:37;  @author: joinpython.com
'''

import sys
import time
for i in range(5):
    print i,
    #sys.stdout.flush()
    time.sleep(1)
# python l01_sys_stdout2.py
# 本是每隔一秒输出一个数字，但现在是循环完才会打印所有结果。如果把sys.stdout.flush()的注释去掉，就会没执行到print就会刷新stdout输出，这对实时输出信息的程序有帮助。