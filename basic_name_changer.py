#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 10:11:18 2018

@author: tyler
"""
from pyne import nucname

element = nucname.name('U-235')

different_nuc_names = ['Uran-235','Copper-64', 'Plut-239', '232-Thor']

nuc_names = ['U-235','Cu-64', 'Pu-239', 'Th-232']

nuc_dict = zip(different_nuc_names, nuc_names)
nuc_translate = {} 
for different_nuc_name,nuc_name in nuc_dict:
    nuc_translate[different_nuc_name] = nuc_name   
print(nuc_translate['232-Thor'])
list(nuc_translate.values())
