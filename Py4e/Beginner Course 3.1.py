# -*- coding: utf-8 -*-
"""
Created on Saturday, ‎May ‎12, ‎2018, ‏‎17:30:23

@author: evan9
"""

'''
list1 = ['Arthur', 50, 'Charles']
list2 = [['Arthur', 95],['Bill', 80],['Charles', 78]]

for i in range(len(list2)):
    for j in range(len(list2[i])):
        print(list2[i][j], end=' ')
    print('\n', end='')
        

for i in range(len(list2)):
    print('Score{}= {}'.format(str(i), list2[i][1]))
'''

'''
for i in range(1,10):
    for j in range(1,10):
        #print('{}*{}={}'.format(i,j,i*j))
        print('%d*%d=%-2d' %(i,j,i*j), end=' ')
        #'%-2d'表示列印佔2字元的整數，並靠左對齊
    #print('-----')
    print('\n')
'''

'''
n = int(input('How many stories are there in this building: '))
if n > 3:
    n += 1
print('Floors that we have: ', end='')
for i in range(1, n + 1):
    if i == 4:
        continue
    else:
        print(i, end=' ')
'''    

'''
#質數=True; 不是質數=False
n = int(input('int n= (n>1) '))
if n == 2:
    print(True)
else:
    for i in range(2,n):
        if n%i == 0:
            print(False)
            break
    else:
        print(True)
'''

score = 0
sum = 0
num = 0
while score != -1:
    num += 1
    score = int(input('Score of student No.{}: '.format(num)))
    sum += score

sum += 1
num -= 1
print('Total score: {}'.format(sum))
print('Student number: {}'.format(num))
average = sum/num
print('Average: {}'.format(average))
    





