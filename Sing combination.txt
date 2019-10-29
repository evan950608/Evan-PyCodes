# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 18:19:05 2019

@author: evan9
"""

import itertools

in_1 = '5\n2 2 3 4 5\n4\n-1'
in_2 = '3\n1 2 3\n0\n3\n1 8 7\n2\n-1'
in_3 = '3\n1 2 3\n1\n3\n1 8 7\n2\n-1'
in_list = in_1.split('\n')
in_list.pop()   # 移除最後一個 就是'-1'

# 把input用成好看的格式
data = [in_list[x: x+3] for x in range(0, len(in_list), 3)]
#print(data)

for trial in data:
    n = int(trial[0])   # 學生人數
    students = [int(i) for i in trial[1].split()]
    students = sorted(students, reverse=True)   # ability由大到小排序
    pick = int(trial[2])    # 選取人數
    
    # itertool.combinations() 列出所有可能組合
    combinations = list(set(itertools.combinations(students, pick)))
    combinations = sorted(combinations, reverse=True)   # 由大到小排序
#    print(combinations)
    
    # 移除不想要的字元後輸出
    for comb in combinations:
        for char in ['(', ',', ')']:
            comb = str(comb).replace(char, '')
        print(comb)
















    