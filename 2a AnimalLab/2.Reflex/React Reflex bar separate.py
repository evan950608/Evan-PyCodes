# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 21:46:59 2019

@author: evan9
"""

import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('React bar.csv')
react = df[df['Type'] == 'react']
reflex = df[df['Type'] == 'reflex']

# In[]
fig = plt.figure(figsize=(14,6))

plt.subplot(1,2,1)
plt.bar(x='Exp', height='Average_time', data=react, yerr='std', capsize=5, color='orange')
plt.ylim(0, 0.6)
plt.ylabel('Average time (s)')

plt.subplot(1,2,2)
plt.bar(x='Exp', height='Average_time', data=reflex, yerr='std', capsize=5)
plt.ylim(0, 0.05)
plt.ylabel('Average time (s)')

#plt.savefig('react reflex bar.png', dpi=200)