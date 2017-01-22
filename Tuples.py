# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 16:46:39 2017

@author: Shreyas
"""

import collections

#Tuples are like Lists. Tuples are Immutable, similar to a string
tuple1 = (1,2,3,4,5,8)
print(tuple1)
print('Max of tuple1 :',max(tuple1))
print('Min of tuple1 :',min(tuple1))
print('Sum of tuple1 :',sum(tuple1))


# Lists -> [] , dictionaries-> { }, tuples = ()  
#We can loop through the tuples
# But no Sort, append, reverse
for iter in tuple1:
    print(iter)
print('What you can do with Tuples : Basically count, index')
print(dir(tuple1))

#Tuples are more efficient

#Tuples and Assignment
(x, y) = ('John', 'James')
print(y)
a,b = (22,44)
print(a)

# d.items() in dictionaries returns list of (Key, value) Tuples
#Tuples are comparable
print((2,1,2) < (4,0,0))

print(('Shreyas', 'Yashas') == ('Yashas', 'Shreyas'))

#Sorting lists of tuples
d = {'a':10,'c':20, 'b':22}
t =d.items()
print('Tuples : ',t)
t = sorted(d.items()) 
print('sorted list of tuples : ',t)

for k, v in sorted(d.items()):
    print(k, v)
    
    


    
c = {'b':10, 'c':48, 'a':36}
list1 = []
#Sorting by Values in reverse order
for k, v in c.items():
    list1.append((v, k))
list1.sort(reverse = True)
print(list1)
    
    
    
    
    
    
    
    
    
    
    









