# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 01:03:10 2017

@author: Shreyas
"""

xfile2 = open('words.txt')
count = 0
for line in xfile2:
    count = count + 1
    print(line)
print ("line count", count)

xfile = open("words.txt")
inp = xfile.read()
print(inp[:440])
print('char count in file :',len(inp))

#Searching through a File
try:
    print('\nIn try Block')
    xfile3 = open('words.txt')
except:
    print('File Cannot be opened ', xfile3)
    exit()
for line in xfile3:
    line = line.strip() 
    if line.startswith('a'):
        print(line)
        
#Searching through a File
fname = input('Enter the File Name : ')
xfile4 = open(fname)
for line in xfile4:
    line = line.strip()
    if not 'is' in line:
        continue
    print(line)

            
            
        
        
            