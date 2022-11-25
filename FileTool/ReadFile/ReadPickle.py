#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Swking
@File  : ReadPickle.py
@Date  : 2020/07/16
@Desc  : 
"""

import pickle

def ReadPickle(path):
    fw = open(path, 'wb+')
    data = pickle.load(fw)
    fw.close()
    return data