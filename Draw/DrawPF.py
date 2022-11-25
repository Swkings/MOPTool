#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Swking
@File  : DrawPF.py
@Date  : 2020/07/15
@Desc  : 
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def DrawPF(DataList, plotLabelList, figTitle='fig', figsize=None, legendTitle=None, axLabelList=None, legendLoc='best', legendFontSize='xx-large', modelList=None):
	if modelList is None:
		modelList = ['science', 'scatter']
	with plt.style.context(modelList):
		if len(DataList[0][0]) == 2:
			if figsize is None:
				fig, ax = plt.subplots()
			else:
				fig, ax = plt.subplots(figsize=figsize)
			for i, data in enumerate(DataList):
				ax.plot(data[:, 0], data[:, 1], label=plotLabelList[i])
			ax.legend(title=legendTitle, loc=legendLoc, fontsize=legendFontSize)
			if axLabelList is not None:
				ax.set(xlabel=axLabelList[0])
				ax.set(ylabel=axLabelList[1])
		elif len(DataList[0][0]) == 3:
			if figsize is None:
				fig = plt.figure()
			else:
				fig = plt.figure(figsize=(8, 8))
			ax = fig.add_subplot(111, projection='3d')
			for i, data in enumerate(DataList):
				ax.plot(data[:, 0], data[:, 1], data[:, 2], label=plotLabelList[i])
			ax.legend(title=legendTitle, loc=legendLoc, fontsize=legendFontSize)
			if axLabelList is not None:
				ax.set(xlabel=axLabelList[0])
				ax.set(ylabel=axLabelList[1])
				ax.set(zlabel=axLabelList[2])
		else:
			if figsize is None:
				fig, ax = plt.subplots()
			else:
				fig, ax = plt.subplots(figsize=figsize)
			for i, data in enumerate(DataList):
				for y in data:
					ax.plot(range(1, len(y) + 1), y, label=plotLabelList[i])
			ax.legend(title=legendTitle, loc=legendLoc, fontsize=legendFontSize)
			if axLabelList is not None:
				ax.set(xlabel=axLabelList[0])
				ax.set(ylabel=axLabelList[1])
		ax.autoscale(tight=True)
		plt.title(figTitle)
		return fig, ax