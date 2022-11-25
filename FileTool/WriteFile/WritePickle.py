#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Swking
@File  : WritePickle.py
@Date  : 2020/07/16
@Desc  : 
"""

import pickle

def WritePickle(path, data):
    with open(path, 'wb+') as fw:
        pickle.dump(data, fw)
    fw.close()