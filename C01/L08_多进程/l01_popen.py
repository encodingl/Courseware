#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2017-10-27 16:02:48;  @author: joinpython.com
'''
from subprocess import Popen, PIPE
from time import sleep


# cmd = "touch /xxx/abc"
# cmd = "df -h"
cmd = "sleep 10"

pcmd = Popen(cmd, stdout=PIPE, stderr=PIPE, shell=True) #开启新进程执行cmd命令
ppid=pcmd.pid        #新开启进程pid
print "ppid:%s" % ppid

# sleep(12)

pcode=pcmd.poll()  #检查子进程  p 是否已经终止，返回 p.returncode 属性
print "pcode:%s" % pcode

pdata = pcmd.communicate() #执行结果详情

pret=pcmd.returncode #子进程退出时返回的状态码
print "pret:%s" % pret

pwait=pcmd.wait()  #等待子进程 p 终止，返回 p.returncode 属性
print "pwait:%s" % pwait

pdata1 = "xd"







print pdata