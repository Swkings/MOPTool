#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Swking
@File  : WriteNumpy.py
@Date  : 2020/07/10
@Desc  : 
"""
import numpy as np

def WriteNumpy(Path, data, fmt='%f', delimiter=' '):
	np.savetxt(Path, data, fmt=fmt, delimiter=delimiter)
