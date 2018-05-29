#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 29 15:08:34 2018

@author: tyler
"""
import numpy as np
from numpy import pi,exp,sqrt
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import matplotlib.animation as animation
x = np.arange(-5, 5, 0.1)
y = np.arange(-5, 5, 0.1)
xx, yy = np.meshgrid(x, y, sparse=True)
z = np.sin(xx**2 + yy**2) / (xx**2 + yy**2)
h = plt.contourf(x,y,z)