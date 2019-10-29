# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 21:22:07 2019

@author: evan9
"""

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('IRE.csv')
x = data.iloc[:, 0]
y_first = data.iloc[:, 1]
y_second = data.iloc[:, 2]
y_ratio = data.iloc[:, 3]

# In[]
fig_1 = plt.figure(figsize=(10,6))
ax_1 = fig_1.add_axes([0.1, 0.1, 0.8, 0.8])
ax_1.plot(x, y_ratio, color='blue', lw=0, marker='o')
ax_1.set_ylim([0, 1.2])
ax_1.set_xlim([0, 25])
ax_1.set_title('Time Delay/ Refractory Period', fontsize=24)
ax_1.set_xlabel('Time Interval (ms)', fontsize=16)
ax_1.set_ylabel('R1/R2 Ratio', fontsize=16)

plt.show()
fig_1.savefig('IRE ratio.png')

# In[]
fig_2 = plt.figure(figsize=(10,6))
ax_2 = fig_2.add_axes([0.1, 0.1, 0.8, 0.8])
ax_2.plot(x, y_first, color='blue', lw=0, marker='o')
ax_2.plot(x, y_second, color='red', lw=0, marker='s')
ax_2.set_title('First & Second Pulse Response', fontsize=20)
ax_2.set_xlabel('Time Interval (ms)', fontsize=16)
ax_2.set_ylabel('Response (mV)', fontsize=16)
ax_2.legend(loc=0, prop={'size': 16})

plt.show()
fig_2.savefig('IRE first second.png')












