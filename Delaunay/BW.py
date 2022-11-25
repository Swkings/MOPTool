#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Swking
@File  : BW.py
@Date  : 2020/07/10
@Desc  : Bowyer-Watson算法
"""

import numpy as np


def Circumcircle(T, coord, superTCoord):
	"""
	已知三点，求外接圆，返回中心坐标center{x, y}，半径R
	(x1-x)²+(y1-y)²=R²
	(x2-x)²+(y2-y)²=R²
	(x3-x)²+(y3-y)²=R²
	@param T: pA, pB, pC
	@param coord:
	@param superTCoord:
	@return:
	"""
	pA, pB, pC = T

	if pA < 0:
		x1, y1 = superTCoord[pA]
		p1 = np.array(superTCoord[pA])
	else:
		x1, y1 = coord[pA]
		p1 = coord[pA]
	if pB < 0:
		x2, y2 = superTCoord[pB]
		p2 = np.array(superTCoord[pB])
	else:
		x2, y2 = coord[pB]
		p2 = coord[pB]

	if pC < 0:
		x3, y3 = superTCoord[pC]
		p3 = np.array(superTCoord[pC])
	else:
		x3, y3 = coord[pC]
		p3 = coord[pC]

	# e = 2 * (x2 - x1)
	# f = 2 * (y2 - y1)
	# g = x2 * x2 - x1 * x1 + y2 * y2 - y1 * y1
	# a = 2 * (x3 - x2)
	# b = 2 * (y3 - y2)
	# c = x3 * x3 - x2 * x2 + y3 * y3 - y2 * y2
	# x = (g * b - c * f) / (e * b - a * f)
	# y = (a * g - c * e) / (a * f - b * e)
	# R = np.sqrt((x - x1) * (y - x1) + (y - y1) * (y - y1))

	a = np.sqrt(np.sum((p1 - p2) ** 2))
	b = np.sqrt(np.sum((p1 - p3) ** 2))
	c = np.sqrt(np.sum((p2 - p3) ** 2))
	S = (1 / 2) * a * b * np.sqrt(1 - ((a ** 2 + b ** 2 - c ** 2) / (2 * a * b)) ** 2)
	if S == 0:
		R = 0
		x, y = x1, y1
	else:
		R = (a * b * c) / (4 * S)
		x = np.linalg.det([[x1 ** 2 + y1 ** 2, y1, 1], [x2 ** 2 + y2 ** 2, y2, 1], [x3 ** 2 + y3 ** 2, y3, 1]]) / (
					2 * np.linalg.det([[x1, y1, 1], [x2, y2, 1], [x3, y3, 1]]))
		y = np.linalg.det([[x1, x1 ** 2 + y1 ** 2, 1], [x2, x2 ** 2 + y2 ** 2, 1], [x3, x3 ** 2 + y3 ** 2, 1]]) / (
					2 * np.linalg.det([[x1, y1, 1], [x2, y2, 1], [x3, y3, 1]]))

	center = [x, y]
	return center, R

def Triangle(pA, pB, pC):
	return sorted([pA, pB, pC])

def Edge(pA, pB):
	if pA > pB:
		return pB, pA
	return pA, pB

def T2E(T):
	return [Edge(T[0], T[1]), Edge(T[1], T[2]), Edge(T[0], T[2])]

def getDistance(coordA, coordB):
	return np.sqrt(np.sum(np.power(coordA - coordB, 2)))

def inCircle(center, r, pCoord):
	return r > getDistance(center, pCoord)


def Delaunay(pSet):
	TBuffer = []

	xMin, yMin = np.min(pSet, axis=0)
	xMax, yMax = np.max(pSet, axis=0)
	# top = [(xMin + xMax) / 2, ((yMax - yMin) * 2) + yMin]
	# left = [top[0] - 2*(top[0] - xMin) - top[0]/100, yMin - top[1]/100]
	# right = [top[0] + 2*(top[0] - xMin) + top[0]/100, yMin - top[1]/100]

	top = [(xMin + xMax) / 2, ((yMax - yMin) * 3) + yMin]
	left = [top[0] - 3 * (top[0] - xMin), yMin - (yMax - yMin)]
	right = [top[0] + 3 * (top[0] - xMin), yMin - (yMax - yMin)]

	superTCoord = {-1: right, -2: left, -3: top}
	superT = Triangle(-1, -2, -3)

	TBuffer.append(superT)

	# ax = drawCoord(pSet)
	# ax = drawTriangle(coord=np.array([top, left, right]), T=[0,1,2], ax=ax)
	# plt.show()

	# 将点逐步加入
	for p in range(len(pSet)):
		EBuffer = []
		pCoord = pSet[p]
		for T in TBuffer[:]:
			center, r = Circumcircle(T, pSet, superTCoord)
			# 删除受影响的三角形，记录边，删除重复的边（包括自身），重新构成三角形
			if inCircle(center, r, pCoord):
				EBuffer.extend(T2E(T))
				TBuffer.remove(T)
		EBuffer = list(filter(lambda x: EBuffer.count(x) == 1, EBuffer))
		for E in EBuffer:
			TBuffer.append(Triangle(E[0], E[1], p))

	# 删除与超级三角形中点相连的三角形
	for T in TBuffer[:]:
		hasP = [p < 0 for p in T]
		if any(hasP):
			TBuffer.remove(T)
	return TBuffer

def Delaunay2CandidateSet(graph, TBuffer):
	candidateSet = {}
	for T in TBuffer:
		e1, e2, e3 = T
		if e1 in candidateSet.keys():
			candidateSet[e1].append([e2, graph[e1][e2]])
			candidateSet[e1].append([e3, graph[e1][e3]])
		else:
			candidateSet[e1] = []
			candidateSet[e1].append([e2, graph[e1][e2]])
			candidateSet[e1].append([e3, graph[e1][e3]])

		if e2 in candidateSet.keys():
			candidateSet[e2].append([e1, graph[e2][e1]])
			candidateSet[e2].append([e3, graph[e2][e3]])
		else:
			candidateSet[e2] = []
			candidateSet[e2].append([e1, graph[e2][e1]])
			candidateSet[e2].append([e3, graph[e2][e3]])

		if e3 in candidateSet.keys():
			candidateSet[e3].append([e1, graph[e3][e1]])
			candidateSet[e3].append([e2, graph[e3][e2]])
		else:
			candidateSet[e3] = []
			candidateSet[e3].append([e1, graph[e3][e1]])
			candidateSet[e3].append([e2, graph[e3][e2]])
	return candidateSet


if __name__ == '__main__':

	from LinKernighan.configure.getGlobalParameters import getParameters
	from LinKernighan.readFiles.readTSP import readTsp2Dict
	from LinKernighan.draw.drawTriangle import *
	from LinKernighan.draw.drawCoord import *
	configureDir = '../configure/configFiles/TSP/'
	configureFile = [configureDir + 'burma14.json', configureDir + 'att48.json', configureDir + 'berlin52.json',
	                 configureDir + 'KroA100.json', configureDir + 'bier127.json', configureDir + 'a280.json',
	                 configureDir + 'att532.json', configureDir + 'pr1002.json']
	configure = getParameters(configureFile[-2])
	tspData = readTsp2Dict(configure['FILE_PATH'])

	coordinates = tspData['NODE_COORD_SECTION'][:, 1:]
	TSet = Delaunay(coordinates)
	ax = drawCoord(coordinates)
	ax = drawTriangle(coord=coordinates, TSet=TSet, ax=ax)
	plt.show()
