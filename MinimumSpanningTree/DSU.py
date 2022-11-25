#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Swking
@File  : dsu.py
@Date  : 2020/05/20
@Desc  : 
"""

class DSU:
	"""
	并查集
	Disjoint Set Union
	"""
	def __init__(self, n):
		self.treeNum = n  # 树的棵树，初始化n颗
		self.size = [1] * n  # 存每棵树的节点数，初始化1个节点
		self.ancestorsNode = [item for item in range(n)]  # 初始化每个节点的祖先是自己

	def getTreeNum(self):
		"""
		获取数的棵树
		"""
		return self.treeNum

	def find(self, i):
		"""
		寻找节点i的祖先
		"""
		while self.ancestorsNode[i] != i:
			i = self.ancestorsNode[i]
		return i

	def isConnect(self, i, j):
		"""
		判断节点i、j是否在同一棵树
		"""
		return self.find(i) == self.find(j)

	def Union(self, i, j):
		"""
		合并i、j所处的树
		两棵树连接成功返回True
		"""
		iAncestor = self.find(i)
		jAncestor = self.find(j)
		if iAncestor == jAncestor:  # 祖先相同，属于同一棵树
			return False
		# 根据树的大小选择合并，小树并入大树
		if self.size[iAncestor] < self.size[jAncestor]:
			self.ancestorsNode[iAncestor] = jAncestor
			self.size[jAncestor] += self.size[iAncestor]
		else:
			self.ancestorsNode[jAncestor] = iAncestor
			self.size[iAncestor] += self.size[jAncestor]
		# 合并后树减少一颗
		self.treeNum -= 1
		return True