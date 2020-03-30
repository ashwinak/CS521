#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 19:09:41 2019

@author: ashwinak

(Count occurrence of numbers) 
Write a program that reads some integers between 1 and 100 and counts the occurrences of each. Here is a sample run of the program:

Enter integers between 1 and 100: 2 5 6 5 4 3 23 43 2
2 occurs 2 times
3 occurs 1 time
4 occurs 1 time
5 occurs 2 times
6 occurs 1 time
23 occurs 1 time
43 occurs 1 time

"""
try:
    import sys
    from collections import Counter
    integers = input("Enter integers between 1 and 100: ").split(" ")
    integers = list(map(int, integers))
    for items in integers:
        if len(integers) > 100:
            sys.exit()
    count = dict(Counter(integers))
    for i,j in count.items():
        if j > 1:
            print (i, "occurs" , j, "times")
        else:
            print (i, "occurs" , j, "time")
except SystemExit:
    print("Integer count exceeded limit")
except ValueError:
    print("Enter only integers seperated by space")
    