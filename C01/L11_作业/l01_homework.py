#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2017-10-30 17:16:05;  @author: joinpython.com
'''

import re
import sys
def get_AnsibleHostsList(hostsfile,group):
    dic = {}
    pattern = r'^\s*\[.+\]'
    try:
        with open(hostsfile) as f:
            for line in f:
                temp = line.split()
                if temp:
                    m = re.search(pattern,line)
                    if (m is not None):
                        g = m.group().strip().strip('[').strip(']')
                        dic[g] = []
                    else:
                        try:
                            dic[g].append(line)
                        except:
                            pass
    except:
        print sys.exc_info()
    
    list_hosts = []
    try:
        for h in dic[group]:
            list_hosts.append(h)
    except:
        pass 
    
    if not list_hosts :
        
        list_hosts = ['ansible hosts not exist']
    return list_hosts

if __name__ == "__main__":
    print get_AnsibleHostsList('/etc/ansible/hosts', "gtest1")
   