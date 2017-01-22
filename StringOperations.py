# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 03:40:23 2017

@author: Shreyas
"""
import math
#String for loop, while loop, in keyword
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

#String slicing
s = "Shreyas Yashas Abhi Ashi Moni Suhas"
print(s[:len(s)+1])
print(s[6:6])
print(s[:])

#String Concateation
a = "Shreyas"
b = "Yashas"
print(a+" "+b)

print('S' in a)
print('Y' in b)

if a< b:
    print("a is less than b")
elif a==b:
    print("a is equal to b")
else :
    print("B is less than a")
    
#String library built-in Functions
print(a.lower())
print(b.lower())

print(a.upper())
print(b.upper())
print("Hi- from Shreyas Yashas".upper())
print(type(a))
print(dir(a))
print(math.pow(2,5))

n = a.find('y')
print(n)
    
greet = a.replace("Shreyas", "Suhas")
print(greet)
    
x= "         Suhas MS   "
x = x.strip()
print(x)
print(x.startswith('Suhas'))
print(x.startswith('s'))

print(len('banana')*7)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


