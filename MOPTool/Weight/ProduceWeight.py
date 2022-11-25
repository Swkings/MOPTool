#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Swking
@File  : ProduceWeight.py
@Date  : 2019/01/12
@Desc  :
"""
from MOPTool.Weight.Permutations import Permutations
import numpy as np

def ProduceWeight(dimension, stepLength):
	"""
	产生某维度，每个维度步长
	:param dimension:
	:param stepLength:
	:return:
	"""
	seq = np.concatenate((np.zeros(stepLength), np.ones(dimension-1)))
	seqAll = Permutations(seq)
	weights = []
	for i in range(seqAll.shape[0]):
		index = np.where(seqAll[i] > 0)[0]
		index += 1
		index1 = np.append(index, dimension+stepLength)
		index2 = np.insert(index, 0, 0)
		weight = ((index1 - index2) - 1) / stepLength
		weights.append(weight)
	return np.array(weights)

if __name__ == '__main__':
	weights = ProduceWeight(3, 6)
	print(len(weights))
