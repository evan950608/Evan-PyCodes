# -*- coding: utf-8 -*-
"""
Created on Sat May 19 17:21:34 2018

@author: evan9
"""

fname = input('Enter file name: ')
#c:\\PyCodes\\File\\filename.txt
#c:\\PyCodes\\File\\mbox-short.txt
try:
    rfile = open(fname)
except:
    print('File cannot be opened: {}'.format(fname))
    input('Press Enter to continue...')
    quit()
    
sumconf = 0    #Sum of X-DSPAM-Confidence
avgconf = 0    #Average of X-DSPAM-Confidence
count = 0      #How many X-DSPAM-Confidence?
target = 'X-DSPAM-Confidence'

for line in rfile:
    if target in line:
        conf = float(line[-6:])
        sumconf += conf
        count += 1
    else:
        continue

avgconf = sumconf / count
#round(n,k)    #四捨六入 #k(int)為小數位數
sumconf = round(sumconf, 4)
avgconf = round(avgconf, 4)
print('Sum of X-DSPAM-Confidence: {}'.format(sumconf))
print('Average of X-DSPAM-Confidence: {}'.format(avgconf))






