#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 01:35:02 2019

@author: ashwinak

(Conversion from kilograms to pounds) 
Write a program that displays the following table (note that 1 kilogram is 2.2 pounds):

"""
kiloToPound = {}
k=1
while k < 200:
    if k % 2 != 0:
        kiloToPound[k] = round(k * 2.2,3)
    k+=1
print ("Kilogram\tPounds")
print("")
for k in kiloToPound:
    print("{}\t\t{}".format(k,kiloToPound[k]))
