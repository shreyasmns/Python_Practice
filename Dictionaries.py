# -*- coding: utf-8 -*-
"""
Created on Tue Jan 17 15:03:32 2017

@author: Shreyas
"""

# Dictionary is a bag of words, each with its own label
# Key-Value pairs, works on the princliple of HASHING
# Dictionaries allows to do  Database like Operations in Python
# Same as Map/ HashMap in Java, No order
purse = dict()
purse['Shreyas'] = 28
purse['Yashas'] = 26
purse['Abhi'] = 18
purse['Ashi'] = 15
purse['Suhas'] = 8
print('\n',purse)   
print(len(purse))

print('\n', 'What all ou can do with dictionaries in Python:')
print(dir(purse), '\n')

print('Keys in dict()   :', purse.keys())
print('Values in dict() :', purse.values())
print('Moni' in purse)

counts = dict()
names = ['Shreyas', 'Yashas', 'Yashas', 'Abhi', 'Yashas','Ashi','Suhas','Yashas']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name]+1
print(counts)
print(counts.get('Yashas', 100))
print(counts.get('moni','moni'))  #get method in dict()


#Loops in dictionaries
for key in counts:
    print(key, counts[key])
print('Printing keys : ', counts.keys())
print('Printing values : ', counts.values())
print('Printing tuples :', counts.items())
    

#Two iteration varieables in loop
print('\n Two Iteration variables : using Items()')
for key, value in counts.items():
    print(key, value)
    