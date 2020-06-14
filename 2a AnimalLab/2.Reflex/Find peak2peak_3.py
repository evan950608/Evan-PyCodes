# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 15:22:29 2019

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


trials = powerlab_txt('JM f.txt')

# In[]
data_lst = []
for trial in trials:
    x = trial.iloc[:, 0]
    y_hammer = trial.iloc[:, 1]
    y_response = trial.iloc[:, 2]
    
    stimulus_max = max(y_hammer)
    response_max = max(y_response)
    response_min = min(y_response)
    peak_to_peak = response_max - response_min
    data_lst.append([stimulus_max, response_max, response_min, peak_to_peak])

data = pd.DataFrame(data_lst, columns=['Stimulus', 'Max_response', 'Min_response', 'Peak_to_peak'])
#data.to_csv('p2p JM f.csv', sep=',', encoding='utf-8')
print(data)
print(data['Peak_to_peak'].idxmax())
print(data.loc[data['Peak_to_peak'].idxmax()])
print('Average p2p: ', data.iloc[:, 3].mean())












