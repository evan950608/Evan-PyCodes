# -*- coding: utf-8 -*-
"""
Created on Sat May 19 23:41:40 2018

@author: evan9
"""

def pause():
    input('Press Enter to continue...')

infname = input('Enter input file name: ')
outfname = input('Enter ouput file name: ')
try:
    infile = open(infname, 'r')
except:
    print('File cannot be opened: {}'.format(infname))
    pause()
    quit()
if '.txt' not in outfname:
    print('Invalid file name: {}'.format(outfname))
    pause()
    quit()
else:
    outfile = open(outfname, 'w')
    
lines = []
for i in infile:
    lines.append(i)
for j in lines:
    j = j.rstrip()
    print(j)
for k in lines:
    outfile.write(k)
outfile.close()

print('\nCopy Completed')
pause()

