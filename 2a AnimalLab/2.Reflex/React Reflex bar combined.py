# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 16:52:03 2019

@author: evan9
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('MRI bar.csv')

plt.figure(figsize=(8,6))
sns.barplot(x='Exp', y='Maximal_response', data=df, hue='Type')
plt.xlabel('Experiment', fontsize=16)
plt.ylabel('Maximal response (mV)', fontsize=16)
plt.legend(fontsize=14)
plt.title('Maximal response', fontsize=20)
plt.show()

plt.figure(figsize=(8,6))
sns.barplot(x='Exp', y='Avg_response', data=df, hue='Type')
plt.xlabel('Experiment', fontsize=16)
plt.ylabel('Average response (mV)', fontsize=16)
plt.legend(fontsize=14)
plt.title('Average response', fontsize=20)
plt.show()
#plt.savefig('Average response', dpi=200)