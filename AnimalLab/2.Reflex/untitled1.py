# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 03:12:44 2019

@author: evan9
"""

import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('React bar.csv')
for i in (5,4,3):
    df.drop(i, inplace=True)


# In[]
plt.figure(figsize=(8,6))
#axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])
plt.ylim(0, 0.7)
#sns_plot = sns.barplot(x='Exp', y='Average_time', data=df, color='Grey')
plt.bar(x='Exp', height='Average_time', data=df, yerr='std', capsize=5)
plt.xlabel('Experiment', fontsize=16)
plt.ylabel('Average time (ms)', fontsize=16)
#fig = sns_plot.get_figure()
#fig.savefig('react bar.png')
plt.show()

# In[]
df.plot(x='Exp ', y='Average_time', kind='bar', yerr='std', capsize=5, figsize=(8,6), ylim=(0,0.7))
