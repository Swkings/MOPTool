#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Swking
@File  : ReadNumpy.py
@Date  : 2020/07/10
@Desc  : 
"""

import numpy as np

def ReadNumpy(Path, dType=float, delimiter=' '):
	data = np.loadtxt(Path, dtype=dType, delimiter=delimiter)
	return data