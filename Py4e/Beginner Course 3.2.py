# -*- coding: utf-8 -*-
"""
Created on Sun May 13 20:44:08 2018

@author: evan9
"""

score = []    #score(list) is an empty list
idsc = 0 #individual score
sum = 0
while idsc != -1:
    idsc = int(input('Student\'s score: '))
    score.append(idsc)    #Add idsc(int) at the back of score(list)

k = len(score)-1
#"-1"is not a student's score, so the number of students == len(score)-1

print('Student Number: {}'.format(k))
for i in range(k):
    sum += score[i]
average = sum/k
print('Average: {}'.format(average))
