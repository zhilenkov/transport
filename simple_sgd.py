# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 22:16:37 2019

@author: Dmitry
"""

import numpy as np

np.random.seed(231)

x = np.random.randint(0, 30, size=(2,3))
c = np.random.randint(3, 11, size=(2,3))

print(x)
print(c)

def stream_sum(x, c):
    return np.sum(np.multiply(x, c))

print(stream_sum(x, c))

print(np.sum(x, 0))