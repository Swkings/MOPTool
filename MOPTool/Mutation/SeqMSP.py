#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Swking
@File  : SeqMSP.py
@Date  : 2019/01/12
@Desc  : 序列单点变异
"""
import numpy as np
import random
import copy


def SeqMSP(data, mp):
	"""
	变异
	:return:
	"""
	if type(data) is list:
		data = np.array(data)
	populationSize = data.shape[0]
	chromosomeLength = data.shape[1]
	newPopulation = np.empty((populationSize, chromosomeLength))
	mpSet = []
	for i in range(populationSize):
		mpSet.append(random.random())
	for i in range(populationSize):
		if mpSet[i] < mp:
			mutationPos = random.sample(range(chromosomeLength), 2)
			data[i][mutationPos[0]], data[i][mutationPos[1]] = data[i][mutationPos[1]], \
			                                                                         data[i][mutationPos[0]]
		newPopulation[i] = data[i]
	return newPopulation

def SeqMSPIndividual(individual):
	if type(individual) is list:
		individual = np.array(individual)
	chromosomeLength = individual.shape[0]
	mutationPos = random.sample(range(chromosomeLength), 2)
	posStart, posEnd = (min(mutationPos), max(mutationPos))
	if random.random() <= 0.5:
		individual[posStart], individual[posEnd] = individual[posEnd], individual[posStart]
	else:
		cutPart = copy.deepcopy(individual[posStart:posEnd + 1])
		individual[posStart:posEnd + 1] = cutPart[::-1]
	return individual


if __name__ == '__main__':
	from MOEA.sample import seqSample as ss
	p = ss.seqSample(10, 10)
	print(p)
	newP = SeqMSP(p, 0.9)
	print(newP)
