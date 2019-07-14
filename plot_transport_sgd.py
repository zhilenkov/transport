# -*- coding: utf-8 -*-
"""
Created on Sun Jun 16 15:36:08 2019

@author: Dmitry
"""

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data.csv", delimiter=',', header=None)

plt.figure()
plt.title("Gradient descent for a transportation problem")
plt.xlabel("Number of iterations")
plt.ylabel("Values of objective function")
plt.plot(data[1], data[0])

plt.savefig("fig_gd_2x3.eps", format='eps')

plt.show()