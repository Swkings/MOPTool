#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Swking
@File  : LatinHyperCube.py
@Date  : 2019/01/01
@Desc  : 生成均匀分布的X向量
"""
import numpy as np
import random

def LatinHyperCube(size, dimension=2, span=None):
	"""
	拉丁超立方采样方法
	:param size: 产生样本个数
	:param dimension: 单个样本的维度
	:param span: 样本向量取值范围span（min， max）
	:return:
	"""
	if span is None:
		span = (np.zeros(dimension), np.ones(dimension))
	sample = np.empty((size, dimension))
	layer = 1/size  # 每个维度的分层范围，分为size层
	for i in range(dimension):
		randSingleDimension = np.empty([size])
		for j in range(size):
			randSingleDimension[j] = np.random.uniform(j*layer, (j+1)*layer, 1)
		np.random.shuffle(randSingleDimension)
		sample[:, i] = randSingleDimension
	sample = sample*(span[1]-span[0])+span[0]
	return sample

if __name__ == '__main__':
	dimension = 2
	min = np.zeros(dimension)
	max = np.ones(dimension)+5
	span = (min, max)
	data = LatinHyperCube(100, dimension, span)
	print(data)
	from mayavi import mlab
	from mpl_toolkits.mplot3d import Axes3D
	import matplotlib.pyplot as plt
	plt.scatter(data[:, 0], data[:, 1], color='red')
	list1 = np.linspace(min[0], max[0], 11)
	plt.xlim((min[0], max[0]))
	plt.ylim((min[0], max[0]))
	plt.xticks(list1)
	plt.yticks(list1)
	plt.grid(True)
	plt.show()
	# mlab.points3d(Result[:, 0], Result[:, 1], Result[:, 2], scale_factor=0.1)
	# # mlab.surf(X, Y, Z)
	# mlab.axes(xlabel='X', ylabel='Y', zlabel='Z')
	# mlab.outline()
	# mlab.colorbar()
	# mlab.show()