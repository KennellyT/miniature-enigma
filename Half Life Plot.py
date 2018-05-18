# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib
matplotlib.rc('font', family='serif', size=14)
import matplotlib.pyplot as plt
from pyne import nucname, nuc_data

import tables as tb
f = tb.open_file(nuc_data)
# get a map between nucleon numbers and half-lives
NuclearName= list(map(lambda x:int(x),f.root.decay.level_list[:]['nuc_id']))
anums = map(nucname.anum, NuclearName)
#anums = map(nucname.anum, f.root.decay.level_list[:]['nuc_id'])
#anums = map(nucname.anum, data.half_life_map.keys())

fig = plt.figure(figsize=(13,7))
plt.semilogy(list(anums),  f.root.decay.level_list[:]['half_life'], 'ko', ms=1, alpha=0.3)
plt.xlabel('A')
plt.ylabel('Half-life [s]')