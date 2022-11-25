#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Swking
@File  : CMetric.py
@Date  : 2020/07/09
@Desc  : 
"""

from MOPTool.Other.Dominate import Dominate


def cMetric(A, B, problemType=0):
	"""
	B中能被A中至少一个解支配的解的数目
	@param A:
	@param B:
	@param problemType: 最小化问题：0， 最大化问题：1
	@return:
	"""
	Cab = []
	for b in B:
		for a in A:
			if Dominate(a, b, problemType) == 1:
				Cab.append(b)
				break
	return len(Cab)*1.0/len(B)

