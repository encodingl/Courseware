#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2017-10-31 11:04:19;  @author: joinpython.com
'''
import ConfigParser
import os

def get_redis_config():
    config = ConfigParser.RawConfigParser()
    dirs = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print dirs
    with open(dirs+'/skipper.conf', 'r') as cfgfile:
        config.readfp(cfgfile)
        host = config.get('redis', 'host')     
        port = config.get('redis', 'port')
        db = config.get('redis', 'db')
        password = config.get('redis', 'password')
        
    if not host:
        host="127.0.0.1"
    if not port:
        port="6379"
    if not db:
        db="0"
    return host,port,db,password



if __name__ == "__main__":
    x = get_redis_config()
    print x