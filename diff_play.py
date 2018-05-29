#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 29 14:58:35 2018

@author: tyler
"""
#https://stackoverflow.com/questions/37632069/python-2d-grid-assigning-values-to-coordinates-in-the-grid
import numpy as np
from numpy import pi,exp,sqrt
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import matplotlib.animation as animation

fig = plt.figure()
ax = fig.gca(projection='3d')
x = np.arange(11)
y = np.arange(11)
X, Y = np.meshgrid(x,y)
Z = np.zeros_like(X)
Z[5][5] = 5
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1)
plt.show()
