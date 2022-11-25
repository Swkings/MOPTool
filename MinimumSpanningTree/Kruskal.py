#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Swking
@File  : Kruskal.py
@Date  : 2020/05/20
@Desc  : 
"""

import numpy as np
from MinimumSpanningTree.DSU import DSU

def kruskal(EdgesList, n, specialNode=None):
	"""
	n为顶点个数
	"""
	# 初始化并查集
	dsu = DSU(n)
	EdgesList = sorted(EdgesList, key=lambda x: x[2])
	EL = []
	for i in range(len(EdgesList)):
		A, B, weight = EdgesList[i]
		if specialNode is not None:
			if A == specialNode or B == specialNode:
				continue
		if dsu.Union(A, B):
			EL.append(EdgesList[i])
		if len(EL) >= n-1:
			return EL
	return EdgesList2EdgesDict(EL)

def EdgesList2EdgesDict(EL):
	EL = sorted(EL, key=lambda x: (x[0], x[1]))
	edgesDict = {}
	# 存每个节点的度
	VArray = np.zeros(len(EL) + 1)
	W = 0
	edgesDict[0] = [0, 0]
	for edge in EL:
		A, B, weight = edge
		if A in edgesDict.keys():
			edgesDict[B] = [A, weight]
		else:
			edgesDict[A] = [B, weight]
		VArray[A] += 1
		VArray[B] += 1
		W += weight
	return edgesDict, VArray, W


if __name__ == '__main__':
	from LinKernighan.TSPTools.TSPTools import *
	edgesInfo = [[0, 1, 28], [0, 5, 10], [1, 2, 16], [1, 6, 14], [2, 3, 12], [3, 4, 22], [3, 6, 18], [4, 5, 25], [4, 6, 24]]
	EL = kruskal(edgesInfo, len(edgesInfo))
	print(EdgesList2EdgesDict(EL))

