# -*- coding: utf-8 -*-
"""
Created on Tue May 29 19:32:46 2018

@author: evan9
"""

def open_text_file():
    import os.path
    
    while True:
        fname = input('Enter file name: ')
        #c:\\PyCodes\\File\\word_count.txt
        is_exists = os.path.isfile(fname)
        if is_exists:
            with open(fname, 'r') as file:
                lines = file.readlines()
            return lines
        else:
            print('Invalid filename:',fname)
            continue

def main():
    lines = open_text_file()
    
    word_count = {}
    for line in lines:
#        line = line.rstrip()
#        print(line)
        line = line.lower()
        words = line.split()
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1
    
    bigword = None
    bigcount = None
    for key,value in word_count.items():
#        print(key,value)
        if bigcount == None or value > bigcount:
            bigcount = value
            bigword = key
    print('Bigword:',bigword)
    print('Bigcount:',bigcount)

    
def pause():
    input('Press enter to continue...')
    
if __name__ == '__main__':
    main()
#    pause()
    
    
    
    
    
    