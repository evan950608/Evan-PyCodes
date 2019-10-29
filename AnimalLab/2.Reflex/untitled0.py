# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 16:40:07 2019

@author: evan9
"""

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r"C:\Users\evan9\OneDrive\Document\GitHub\Evan-Python-Basics\AnimalLab\2.Reflex\MSI.csv")
#data = data[data.iloc[:,0] < 0.025]
x = data.iloc[:, 0]
y1 = data.iloc[:, 1] / 5.0
y2 = data.iloc[:, 2]

fig = plt.figure(figsize=(10,7))     # frameon=False
axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])
axes.plot(x, y1, color='blue', lw=2)
axes.plot(x, y2, color='red', lw=2)
axes.set_xlabel('Time (s)', fontsize=16)
axes.set_ylabel('Response (mV)', fontsize=16)
#axes.set_title('Stimulus = {} V', fontsize=20)

plt.show()
#fig.savefig('MSI.png', dpi=200)
