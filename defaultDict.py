# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 03:40:23 2017

@author: Shreyas
"""


fruit= 'Pine Apple'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print (index, letter)
    index += 1
        
str = "aaaaaaaaaaaaaaancschbscbsddbdjbasfbsajasjsajbjsabdhasbajabjjab"
count=0
for x in str:
    if x =='a':
        count += 1
print(count)

s = "Shreyas Yashas Abhi Ashi Moni Suhas"
print(s[:len(s)+1])
print(s[6:6])
print(s[:])