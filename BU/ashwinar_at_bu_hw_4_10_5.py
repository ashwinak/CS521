#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 22:38:06 2019

@author: ashwinak

(Print distinct numbers) 
Write a program that reads in numbers separated by a space in one line and displays distinct numbers 
(i.e., if a number appears multiple times, it is displayed only once). 
(Hint: Read all the numbers and store them in list1. 
Create a new list list2. Add a number in list1 to list2. If the number is already in the list, ignore it.) 
Here is the sample run of the program:
    
Enter ten numbers: 1 2 3 2 1 6 3 4 5 2
The distinct numbers are: 1 2 3 6 4 5

"""

try:
    import sys
    list1 = input("Enter ten numbers: ").split(" ")
    list1 = list(map(int, list1))
    list2 = list(set(list1))
    for items in list1:
        if len(list1) > 10:
            sys.exit()
    print("The distinct numbers are:",end=" ")
    for p in list2: print (p,end=" ")
except TypeError:
    print("Enter only 10 integers")
except SystemExit:
    print("Integer count exceeded limit")  
except ValueError:
    print("Enter only integers seperated by space")  
        