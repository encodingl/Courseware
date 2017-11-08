#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
Create on 2017-11-08 16:47:48;@author:joinpython.com
'''

import sys
try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except IOError as e:
    print "I/O error({0}): {1}".format(e.errno, e.strerror)
except ValueError:
    print "Could not convert data to an integer."
except:
    print "Unexpected error:", sys.exc_info()[0]
    raise
print "over"
