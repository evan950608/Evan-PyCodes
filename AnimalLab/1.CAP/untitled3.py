# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 20:10:31 2019

@author: evan9
"""

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('THfinish_edited.csv')
x = data.iloc[:, 0]
y = data.iloc[:, 1]

fig = plt.figure(figsize=(10,6))
axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])
axes.plot(x, y, color='blue', lw=0, marker='o', markersize=8)
axes.set_ylim([0, 3])
axes.axvline(x=0.580, color='black', ls='--')
axes.axvline(x=0.924, color='black', ls='--')
axes.axhline(y=2.070, color='red', ls='--')

axes.set_xlabel('Stimulus intensity (mV)', fontsize=16)
axes.set_ylabel('Response (mV)', fontsize=16)
axes.set_title('Threshold & MSI', fontsize=24)

plt.show()
fig.savefig('Threshold MSI2.png', dpi=200)


