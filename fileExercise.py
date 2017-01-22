# -*- coding: utf-8 -*-
"""
Created on Mon Jan 16 20:00:10 2017

@author: Shreyas
"""

fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    line = line.rstrip()
    print(line)