#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 24 08:28:02 2018

@author: tyler
"""
from pyne import data
from pyne import nucname

s = data.decay_data_children(922350000)
U235 = nucname.id('U-235')
unk = nucname.name(902310000)
######### Decay chain
U235 = nucname.id('U-235')

IDS = [922350000]
gens = 7
generation = [0]
parent_to_child = []
parent_text = []
j = 0
for i in range(gens):
    iso = IDS[i]
    child = data.decay_data_children(iso)
    nums =len(child)
    if nums ==1:
        IDS.append(child[0])
        j+=1
        generation.append(j)
        parent_to_child.append(str(iso)+'-->'+str(child[0]))
        parent_text.append(str(nucname.name(IDS[i]))+'-->'+str(nucname.name(child[0])))
    if nums ==2:
        IDS.append(child[0])
        parent_to_child.append(str(iso)+'-->'+str(child[0]))
        parent_text.append(str(nucname.name(IDS[i]))+'-->'+str(nucname.name(child[0])))
        IDS.append(child[1])
        parent_to_child.append(str(iso)+'-->'+str(child[1]))
        parent_text.append(str(nucname.name(IDS[i]))+'-->'+str(nucname.name(child[1])))
        j+=1
        generation.append(j)
print('Parent to child relationship:' + str(parent_text))

print(parent_to_child)
print('generations:' + str(generation))
print('list of nucname.ids:'+str(IDS))