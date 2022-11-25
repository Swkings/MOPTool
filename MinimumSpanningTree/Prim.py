#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Swking
@File  : Prim.py
@Date  : 2020/05/20
@Desc  : 
"""

import numpy as np
import heapq as hq


def prim(graph, root, specialNode=None):
	"""
	Runtime:
		O(mn) with `m` edges and `n` vertices
	graph: {
			a ：{b:weight, c:weight}
			b ：{a:weight, c:weight}
			c ：{a:weight, b:weight}
			}
	"""
	edgesDict = {}
	# 存每个节点的度
	VArray = np.zeros(len(graph))
	W = 0
	lowCost = [np.inf]*len(graph)
	lowCostParent = [root]*len(graph)  # 标记对应lowCost的父节点
	# 以root为起点，初始化lowCost 和 lowCostParent
	for node in graph[root].keys():
		lowCost[node] = graph[root][node]
	if specialNode is not None:
		lowCostParent[specialNode] = -1
	lowCostParent[root] = -1
	# 初始化root节点的父节点为其本身，weight为0
	edgesDict[root] = [root, 0]
	parentNode = root
	for i in range(len(graph)):
		minCost = np.inf
		selectVex = -1
		for node in range(len(lowCost)):
			if lowCostParent[node] != -1 and lowCost[node] < minCost:
				minCost = lowCost[node]
				selectVex = node
		if selectVex != -1:
			edgesDict[selectVex] = [lowCostParent[selectVex], minCost]
			VArray[selectVex] += 1
			VArray[lowCostParent[selectVex]] += 1
			W += minCost
			parentNode = selectVex
			# 标记该点被选
			lowCostParent[selectVex] = -1
			# 更新lowCost和lowCostParent
			for j in range(len(lowCost)):
				if lowCostParent[j] != -1 and j in graph[parentNode].keys():
					if graph[parentNode][j] < lowCost[j]:
						lowCost[j] = graph[parentNode][j]
						lowCostParent[j] = parentNode
	return edgesDict, VArray, W


def prim_heap(graph, root, specialNode=None):
	edgesDict = {}
	# 存每个节点的度
	VArray = np.zeros(len(graph))
	W = 0
	visited_parent = [root]*len(graph)
	if specialNode is not None:
		visited_parent[specialNode] = -1
	#  [weight, 当前节点, 父节点]
	queue = [[0, root, root]]
	hq.heapify(queue)
	while queue:
		# 每次弹出weight最小的点
		selectNode = hq.heappop(queue)
		weight = selectNode[0]
		curNode = selectNode[1]
		parentNode = selectNode[2]
		# 判断当前点是否被找过
		if visited_parent[curNode] == -1:
			continue
		visited_parent[curNode] = -1
		# 结果返回为{node: [parentNode, weight]}
		edgesDict[curNode] = [parentNode, weight]
		if curNode != parentNode:
			VArray[curNode] += 1
			VArray[parentNode] += 1
		W += weight
		# 重置父节点
		parentNode = curNode
		# 将当前节点的连接点进堆
		for node in graph[parentNode].keys():
			if visited_parent[node] != -1:
				hq.heappush(queue, [graph[parentNode][node], node, parentNode])
	return edgesDict, VArray, W



if __name__ == '__main__':
	from LinKernighan.TSPTools.TSPTools import *

	edgesInfo = [[0, 1, 28], [0, 5, 10], [1, 2, 16], [1, 6, 14], [2, 3, 12], [3, 4, 22], [3, 6, 18], [4, 5, 25], [4, 6, 24]]
	VL = EdgesList2AdjacencyList(edgesInfo)
	print(VL)
	MST = prim(VL, 0)
	print(MST)
	print(VL)
	MST_Heap = prim_heap(VL, 0)
	print(MST_Heap)
