#! /usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2017-10-30 10:55:52;  @author: joinpython.com
'''

import shutil
shutil.copyfile('data.db', 'archive.db')
shutil.move('/build/executables', 'installdir')
shutil.rmtree("/tmp/t1")