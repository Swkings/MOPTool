#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Swking
@File  : Vector.py
@Date  : 2020/07/10
@Desc  : 
"""

import numpy as np

def vcPlus(a, b):
	'''
	向量加
	:param a:
	:param b:
	:return:
	'''
	if type(a) is list or type(b) is list:
		a = np.array(a)
		b = np.array(b)
	return a + b

def vcMinus(a, b):
	'''
	向量减
	:param a:
	:param b:
	:return:
	'''
	if type(a) is list or type(b) is list:
		a = np.array(a)
		b = np.array(b)
	return a - b

def vcTimes(a, b):
	'''
	向量内积
	:param a:
	:param b:
	:return:
	'''
	if type(a) is list or type(b) is list:
		a = np.array(a)
		b = np.array(b)
	return np.sum(a * b)

def vcLength(a):
	'''
	向量模，二阶范数
	:param a:
	:return:
	'''
	if type(a) is list:
		a = np.array(a)
	return np.abs(np.sqrt(vcTimes(a, a)))

def vcUnit(a):
	'''
	向量单位化
	:param a:
	:return:
	'''
	if type(a) is list:
		a = np.array(a)
	if vcLength(a) < 1/(10e10):
		return a
	return a / vcLength(a)

def isOrthogonal(a, b):
	'''
	判断向量是否正交（垂直）
	:param a:
	:param b:
	:return:
	'''
	if type(a) is list or type(b) is list:
		a = np.array(a)
		b = np.array(b)
	if vcTimes(a, b) < 1/(10e8):
		return True
	return False

def getOrthogonalVector(matrix):
	'''
	获取法向量（正交向量）
	:param matrix:
				dimension=2时：1*dimension
				dimension=3时：2*dimension
				dimension>=3时：dimension*dimension
	:return:
	'''
	# matrix = np.matrix(matrix)
	if type(matrix) is list:
		matrix = np.array(matrix)
	if matrix.shape[1] == 2:
		x = matrix[0][0]
		y = matrix[0][1]
		if x == y and x == 0:
			print("一个点的法向量有无数个！")
			return vcUnit([1, 1])
		elif x==0 and y!=0:
			return np.array([1, 0])
		elif y==0 and x!=0:
			return np.array([0, 1])
		else:
			return vcUnit([-y/x, 1])
	elif matrix.shape[1] == 3:
		'''
		x1   |y1  < z1|  ( x1 >  y1 )  z1
		x2   |y2  < z2|  ( x2 >  y2 )  z2
		'''
		x1, y1, z1 = matrix[0][0], matrix[0][1], matrix[0][2]
		x2, y2, z2 = matrix[1][0], matrix[1][1], matrix[1][2]
		a = y1 * z2 - y2 * z1
		b = z1 * x2 - z2 * x1
		c = x1 * y2 - x2 * y1
		vector = [a, b, c]
		if c < 0:
			vector = np.array(vector) * -1
		return vcUnit(vector)
	else:
		U, sigma, VT = np.linalg.svd(matrix)
		U = U.real
		sigma = sigma.real
		VT = VT.real
		index = np.argmin(sigma)
		vector = VT[index, :]
		if vector[-1] < 0:
			vector = vector * -1
		r = np.sum(matrix * VT[index, :], 1)
		# for i in r:
		# 	if i > 1/10e8:
		# 		print("vector不正交！")
		return vcUnit(vector)
	return vcUnit(np.ones(matrix.shape[1]))

def angle(a, b, isOrthogonal=False, measure=1):
	"""
	求向量夹角
	:param a: 一维向量
	:param b: 一维向量
	:param isOrthogonal:
						False: 非正交向量（法向量）求角 cos(alpha) = cos<a, b> = a·b / |a||b|
						True:  正交向量（法向量）求角  sin(alpha) = cos<a, b> = a·b / |a||b|
	:param measure:
				1: 角度制
				2: 弧度制
	:return:
	"""

	if vcTimes(a, b)==0:
		cosAngle = 0
	else:
		cosAngle = vcTimes(a, b) / (vcLength(a) * vcLength(b))
	alpha = 0
	if isOrthogonal:
		alpha = np.arcsin(cosAngle)
	else:
		alpha = np.arccos(cosAngle)
	if measure==1:
		return alpha*180/np.pi
	else:
		return alpha

if __name__ == '__main__':
	popY = np.zeros((12, 2))
	popY[0] = np.array([1, 6])
	popY[1] = np.array([1, 5])
	popY[2] = np.array([2, 4])
	popY[3] = np.array([2.5, 3])
	popY[4] = np.array([3, 2])
	popY[5] = np.array([4, 1])
	popY[6] = np.array([5, 1])
	popY[7] = np.array([6, 1])
	popY[8] = np.array([2, 6])
	popY[9] = np.array([3, 5])
	popY[10] = np.array([4, 5])
	popY[11] = np.array([5, 3])
	v0_7 = popY[7] - popY[0]
	print(v0_7)
	v0_7Orthogonal = getOrthogonalVector(np.array([v0_7]))
	print(v0_7Orthogonal)
	print(isOrthogonal(v0_7, v0_7Orthogonal))
	angleList = []
	for ind in popY:
		v0_ind = ind - popY[0]
		angleList.append(angle(v0_ind, v0_7Orthogonal, isOrthogonal=True, measure=1))
	print(angleList)
