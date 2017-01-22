# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 20:33:47 2017

@author: Shreyas
"""

#Lists are sorrounded by square brackets
#List element can be any object, even another list
#List can be empty
import collections

list = ['Shreyas', 44, 44.999999999999999]
print(list)

list1 = ['Shreyas', 44, [44,'Yashas']]
print(list1)

brothers = ['Shreyas','Yashas', 'Abhi', 'Ashi', 'Moni', 'Suhas']
for x in brothers:
    print('Hi, Take care ',x , '. Love you !!')
brothers[2]='Abhishek'
print(brothers[2])
print('Length of Brothers :',len(brothers))

#Strings are Immutable, Lists are Mutable
#range function
print(range(len(brothers)))
print (range(10))

for i in range(len(brothers)):
    bro = brothers[i]
    print('hello my Dear Brother',bro)

    
#List concatentation using +
lista = [1,2,3,4]
listb = [5,6,7,8]
num = lista[2]
listc = lista + listb
print(listc)    
list1 = [1,2,3,4,5,6,7,8,9,10,11,12]
print('\n Type of object is:', type(list1))
print('\n Operations you can do with list :', dir(list1))
print(list1[:6])

newlist = [1,2,3,4,5,6]
newlist.append(10)
newlist.append(22)
print(newlist)
print('Is 8 present in our list :', 8 not in newlist)
print('Is 4 present in our list :', 4 in newlist)



brothers = ['Shreyas','Yashas', 'Abhi', 'Ashi', 'Moni', 'Suhas']
brothers.sort()
print('Sorted list of Brothers :',brothers)

nums = [10, 200675, 35535, 4464, 5, 684848, 80, 4, 565112, 124244]
print('\nlength of nums :',len(nums))
print('max of nums : ', max(nums))
print('min of nums :', min(nums))
print('sum of nums :', sum(nums))
print('avg of nums :',sum(nums)/len(nums))

sbc = 'My name is ShreyasMN'
sbclist = sbc.split()
print('string to list: ',sbclist)

abc = 'This; is; an; example'
abclist = abc.split(';')
print(abclist)





















    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    