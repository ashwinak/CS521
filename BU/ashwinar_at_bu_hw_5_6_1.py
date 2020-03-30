#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 17:11:05 2019

@author: ashwinak

(Math: pentagonal numbers) 
A pentagonal number is defined as n(3n - 1)/2 for n = 1, 2..., and so on. 
So, the first few numbers are 1, 5, 12, 22,....
Write a function with the following header that returns a pentagonal number:
def getPentagonalNumber(n):
Write a test program that uses this function to display the first 100 pentagonal
numbers with 10 numbers on each line.

"""
def getPentagonalNumber(n):
    n = n *(3*n - 1)/2
    return int(n)

list1 = [getPentagonalNumber(i) for i in range(101)]
list1.remove(0)

for i,j in zip(range(0,101,10),range(10,101,10)):
    #print (len(list1[i:j]))
    print (', '.join(map(str, list1[i:j]))) 
