# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 20:00:46 2019

@author: Dmitry
"""

import numpy as np

def dualf(c, u, v, a, b, t=0.5, prevsg=0):
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
    idxi = np.random.choice(range(len(i)), p = i/np.sum(i))
    idxj = np.random.choice(range(len(j)), p = j/np.sum(j))
    veci[idxi] = i[idxi]
    vecj[idxj] = j[idxj]
    wsg = np.concatenate((veci - a, vecj - b), axis=0)
    g = np.concatenate((-a + i, -b + j), axis=0)
    un = u + veci - a
    vn = v + vecj - b
    xn = np.concatenate((un, vn))
    mavwsg = t*wsg + (1-t)*prevsg
    return np.array([un, vn, xn, wsg, g, mavwsg])

c = np.array([[3, 4, 6], [2, 9, 1]])
a = np.array([30, 50])
b = np.array([20, 40, 20])

u = np.array([-1, 1])
v = np.array([1, -10, -10])

p = np.sum(a)

print(dualf(c, u, v, a, b, t=0.3))
