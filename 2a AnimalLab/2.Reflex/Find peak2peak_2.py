# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 18:15:59 2019

@author: evan9
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def powerlab_txt(filepath):
    rfile = open(filepath)
    file_str = rfile.read()
    trials_str =[i.split('\n') for i in file_str.split('Interval')]
    del(trials_str[0])
    
    indices = np.arange(5, -1, -1)      # [5,4,3,2,1,0]
    for trial in trials_str:
        for i in indices:
            del(trial[i])
        del(trial[len(trial) - 1])
    
    dfs = []
    for trial in trials_str:
        for i in range(len(trial)):
            trial[i] = trial[i].split('\t')
            trial[i] = [float(j) for j in trial[i]]
        df = pd.DataFrame(trial)
#        df.drop(len(df)-1, inplace=True)
        dfs.append(df)
    
    return dfs


dfs = powerlab_txt('JM f.txt')

data_lst = []
for trial in dfs:
    x = trial.iloc[:, 0]
    y_hammer = trial.iloc[:, 1]
    y_response = trial.iloc[:, 2]
    
    stimulus_max = max(y_hammer)
    response_max = max(y_response)
    response_min = min(y_response)
    peak_to_peak = response_max - response_min
    data_lst.append([stimulus_max, response_max, response_min, peak_to_peak])
    
data = pd.DataFrame(data_lst, columns=['Stimulus', 'Max_response', 'Min_response', 'Peak_to_peak'])
data.to_csv('p2p JM f.csv', sep=',', encoding='utf-8')
print(data)

#    fig = plt.figure(figsize=(10,7))     # frameon=False
#    axes = fig.add_axes([0.1, 0.1, 0.8, 0.8])
#    axes.plot(x, y, color='blue', lw=2)
#    axes.set_xlabel('Time (s)', fontsize=16)
#    axes.set_ylabel('Response (mV)', fontsize=16)
#    
#    plt.show()















