#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 19 17:34:37 2018

@author: tyler
"""
#https://stackoverflow.com/questions/28974818/heat-diffusion-on-a-2d-plate-python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

dt=0.1
dx=0.1

L=50                        # length of the plate
B=50                        # width of the plate


#heating device shaped like X
Gr=np.eye(10)*2000
for iGr in range(10):
    Gr[iGr,-iGr-1]=2000

# Function to set M values corresponding to non-zero Gr values
def assert_heaters(M, Gr):
    M[20:30,10:20] = np.where(Gr > 0, Gr, M[20:30,10:20])
    M[20:30,30:40] = np.where(Gr > 0, Gr, M[20:30,30:40])

a = np.zeros([10,10])
a[:,:] =100
a[:2,0:2] =0
a[:2,8:10] =0
a[8:10,0:2] =0
a[8:10,8:10] =0
def assert_sq_heaters(M1, a):
    M1[20:30,10:20] = np.where(a > 0, a, M1[20:30,10:20])
    M1[20:30,30:40] = np.where(a > 0, a, M1[20:30,30:40])


M=np.zeros([L,B])           # matrix
assert_heaters(M, Gr)

M1=np.zeros([L,B])  
assert_sq_heaters(M1, a)

# Build MM, a list of matrices, each element corresponding to M at a given step
T = np.arange(0,10,dt)
MM = []
for i in range(len(T)):
    for j in range(1,L-1):
        for i in range(1,B-1):
            k=0.5  # default k
            if 20<j<30:
                # holes for liquid
                if 27<i<34 or 25<i<23: k=0

            #dm = k * ((dt)/dx**2) * (M[i,j+1] + M[i,j-1] - 2*M[i,j]) + \
            #     k * ((dt)/dx**2) * (M[i+1,j] + M[i-1,j] - 2*M[i,j])
            #M[i,j] += dm
            M1[i,j] = (M1[i-1,j] + M1[i+1,j] + M1[i,j-1] + M1[i,j+1])/4

    # Re-assert heaters
    assert_sq_heaters(M1,a)

    MM.append(M1.copy())






fig = plt.figure()
pcm = plt.pcolormesh(MM[0])
plt.colorbar()

# Function called to update the graphic
def step(i):
    if i >= len(MM): return
    pcm.set_array(MM[i].ravel())
    plt.draw()
#anim = FuncAnimation(fig, step, frames=100, interval=50)
anim = FuncAnimation(fig, step, interval=100)
plt.show()
