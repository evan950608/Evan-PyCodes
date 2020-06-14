# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 17:42:08 2019

@author: evan9
"""

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('JM react.csv')      #'JM react.csv'
data = data[data.iloc[:, 0] < 0.5]
x = data.iloc[:, 0]
y_hammer = data.iloc[:, 1]
y_response = data.iloc[:, 2]

stimulus_max = max(y_hammer)
#data[data.iloc[:, 1] == stimulus_max]
response_max = max(y_response)
response_min = min(y_response)
peak_to_peak = response_max - response_min

fig = plt.figure(figsize=(10,6))     # frameon=False
axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])
#axes.plot(x, y_hammer / 5, color='blue', lw=2)
axes.plot(x, y_response, color='blue', lw=1)
axes.axvline(x=0.0021, color='black', ls='--')
axes.axvline(x=0.2416, color='black', ls='--')
axes.set_xlabel('Time (s)', fontsize=16)
axes.set_ylabel('Response (mV)', fontsize=16)

plt.show()
#fig.savefig('JM react.png', dpi=200)

print('''Stimulus intensity: {}
Response Max: {}
Response Min: {}
Peak to peak: {}'''.format(stimulus_max, response_max, response_min, peak_to_peak))


