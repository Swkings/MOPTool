#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Swking
@File  : Dominate.py
@Date  : 2020/07/10
@Desc  : 
"""

def Dominate(A, B, problemType=0):
	"""
	A是否支配B
	@param A: 解A 一维
	@param B: 解B 一维
	@param problemType: 最小化问题：0， 最大化问题：1
	@return:
			1：A支配B
			0：A、B互不支配
			-1：B支配A
	"""
	ABetterCount = 0
	BBetterCount = 0
	equalCount = 0
	for i in range(len(A)):
		if A[i] < B[i]:
			ABetterCount += 1
		elif B[i] < A[i]:
			BBetterCount += 1
		else:
			equalCount += 1
		if ABetterCount>0 and BBetterCount>0:
			return 0
	if (ABetterCount+equalCount == len(A)) and ABetterCount>0:
		if problemType == 0:
			return 1
		else:
			return -1
	elif (BBetterCount+equalCount) == len(A) and BBetterCount>0:
		if problemType == 0:
			return -1
		else:
			return 1
	else:
		return 0