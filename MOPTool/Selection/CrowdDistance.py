#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Swking
@File  : CrowdDistance.py
@Date  : 2021/05/17
@Desc  : 
"""

import numpy as np

def CrowdDistance(Y, N):
	"""
	拥挤距离从Y中选择N个个体
	:param Y:
	:param N:
	:return: index
	"""
	if type(Y) is list:
		Y = np.array(Y)
	Size = len(Y)
	if Size<=N:
		return np.array(range(N))
	ObjNum = len(Y[0])
	Dis = np.zeros(Size)
	for i in range(ObjNum):
		index = np.lexsort([Y[:, i]])
		for j in range(Size):
			if j == 0 or j == Size-1:
				Dis[index[j]] += np.inf
			else:
				Dis[index[j]] += (Y[index[j+1]][i] - Y[index[j-1]][i])
	index = np.argsort(-Dis)
	return index[:N]