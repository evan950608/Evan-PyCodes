# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 13:45:07 2019

@author: evan9
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

lst1 = [0.4, 0.5, 0.8, 0.9, 1.0, 1.1, 1.2]
lst2 = [0.924, 1.036, 1.156]
lst3 = [9, 14, 19]

for i in lst3:
    data = pd.read_csv('no{}.csv'.format(i))
    data = data[data.iloc[:,0] < 0.025]
#    data.columns = ['Time', 'Response']
#    x = data['Time']
#    y = data['Response']
    x = data.iloc[:, 0]
    y = data.iloc[:, 1]
#    print('Stimulus = {}'.format(max(data.iloc[:, 2])))
    
    fig = plt.figure(figsize=(10,7))
    axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])
    axes.plot(x, y, color='blue', lw=2)
    axes.set_xlabel('Time (s)', fontsize=16)
    axes.set_ylabel('Response (mV)', fontsize=16)
#    axes.set_title('Stimulus = {} V'.format(i), fontsize=20)
    
    plt.show()
    fig.savefig('no{}.png'.format(i), dpi=200)












