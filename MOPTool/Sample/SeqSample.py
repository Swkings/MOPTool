#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author: Swking
@File  : SeqSample.py
@Date  : 2019/01/13
@Desc  : 
"""
import numpy as np
import random

def SeqSample(size, seqLength):
	population = np.zeros((size, seqLength), np.int)
	for i in range(size):
		chromosome = random.sample(range(seqLength), seqLength)
		population[i] = chromosome
	return population

if __name__ == '__main__':
	p = SeqSample(10, 10)
	print(p)