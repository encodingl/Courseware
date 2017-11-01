#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2017-10-31 11:17:58;  @author: joinpython.com
'''

from l02_homework import get_redis_config
import redis


class RedisLock():
    def __init__(self,channel_name):
        self.channel_name=channel_name
        redis_host,redis_port,redis_db,redis_password = get_redis_config()
        self.conn = redis.Redis(host=redis_host,db=redis_db,port=redis_port,password=redis_password)         
    def lock(self):
        self.conn.set(self.channel_name,"1")
    def unlock(self):
        self.conn.set(self.channel_name,"0") 
    def get_channel_value(self):
        return self.conn.get(self.channel_name)
    def test(self,tchn):
        return self.conn.get(tchn)
    
if __name__ == "__main__":
    r1=RedisLock(channel_name="chn001")
    cv = r1.get_channel_value()
    print cv
    r1.lock()
    cv = r1.get_channel_value()
    print cv
    r1.unlock()
    cv = r1.get_channel_value()
    print cv
    
