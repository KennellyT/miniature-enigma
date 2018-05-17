# -*- coding: utf-8 -*-
"""
Created on Wed May 16 14:23:23 2018

@author: tyler
"""
import numpy as np
import matplotlib.pyplot as plt 
time = np.arange(0,100,1)
a = 100
b=1
c=2
d=3
z = [b,c,d]
counts = []
for i in time:
    x = np.random.choice(z)
    if x == b:
        counts.append(1)   
    if x == c:
        counts.append(2)
    if x ==d:
        counts.append(3) 
print(counts)
w = [[x,counts.count(x)] for x in set(counts)]
print(w)
only1 = [0 if x!=1 else x for x in counts]
only2 = [0 if x!=2 else x for x in counts]
only3 = [0 if x!=3 else x for x in counts]
o1= np.cumsum(only1)
o2= np.cumsum(only2)/2 #since cum sum adds by number not object
o3= np.cumsum(only3)/3 #since cum sum adds by number not object
Probability= w[0][1],w[1][1],w[2][1]
plt.hist(counts)
plt.grid(True)
plt.show()
plt.plot(time,o1,label='b')
plt.plot(time,o2,label='c')
plt.plot(time,o3,label='d')
plt.legend()
plt.grid()
plt.show()
print("b:",str(((w[0][1])/a)*100)+'%')
print("c:",str(((w[1][1])/a)*100)+'%')
print("d:",str(((w[2][1])/a)*100)+'%')