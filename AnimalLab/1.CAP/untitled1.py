# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 01:18:43 2019

@author: evan9
"""

import pandas as pd
import numpy as np

rfile = open('MSI 0.8-8.txt')
text = rfile.read()
pulses = text.split('Interval')

all_df = []
for pulse in pulses:
    for line in pulse.split('\n'):
        i = 0
        pulse_df = pd.DataFrame(columns=['Time', 'Ch1', 'Ch2'])
        for line in pulses[1].split('\n'):
            if line.startswith('-0') or line.startswith('0'):
                print(line)
                pulse_df.loc[i] = line.rstrip().split('\t')
                i += 1
        all_df.append(pulse_df)