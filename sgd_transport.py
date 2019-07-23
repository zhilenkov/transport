# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 20:00:46 2019

@author: Dmitry
"""

import numpy as np
import matplotlib.pyplot as plt

def dualf(c, u, v, a, b, p, t=0.5, prevsg=0, trig_measure=True):
    matu = np.tile(u, (len(v), 1)).T
    matv = np.tile(v, (len(u), 1))
    r = matu + matv + c
    boolr = r < 0
    res = r * boolr * p
    res = np.sum(res)
    i = np.sum(p * boolr, axis=1)
    j = np.sum(p * boolr, axis=0)
    veci = np.zeros(len(i))
    vecj = np.zeros(len(j))
    if trig_measure:
        if (np.sum(i) != 0.) and (np.sum(j) != 0.):
            idxi = np.random.choice(range(len(i)), p = i/np.sum(i))
            idxj = np.random.choice(range(len(j)), p = j/np.sum(j))
            veci[idxi] = i[idxi]
            vecj[idxj] = j[idxj]
    else:
        idxi = np.random.choice(range(len(i)), p = np.array([1/len(i)]*len(i)))
        idxj = np.random.choice(range(len(j)), p = np.array([1/len(j)]*len(j)))
        veci[idxi] = i[idxi]
        vecj[idxj] = j[idxj]
    wsg = np.concatenate((veci - a, vecj - b), axis=0)
    g = np.concatenate((-a + i, -b + j), axis=0)
    wsgu = veci - a
    wsgv = vecj - b
    mavwsg = t*wsg + (1-t)*prevsg
    return np.array([wsgu, wsgv, wsg, g, mavwsg, (res - np.dot(a, u) - np.dot(b, v))])

c = np.array([[3., 4., 6.], [2., 9., 1.]])
a = np.array([30., 50.])
b = np.array([20., 40., 20.])

u = np.array([-1., 1.])
v = np.array([1., -10., -10.])

p = np.sum(a)

# print(dualf(c, u, v, a, b, t=0.3, prevsg=0))

mavwsg = np.concatenate((-a, -b), axis=0)
alph = 1e-4
y = []

for it in range(10000):
    res = dualf(c, u, v, a, b, p, t=0.7, prevsg=mavwsg, trig_measure=False)
    u += alph*res[0]
    v += alph*res[1]
    wsg = res[2]
    g = res[3]
    mavwsg = res[4]
    obj = res[5]
    y.append(obj)
    
print(y[-1])

plt.figure()
plt.plot(list(range(len(y))), y)
