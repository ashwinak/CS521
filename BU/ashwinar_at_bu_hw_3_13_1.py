#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 00:58:13 2019

@author: ashwinak

(Remove text) 
Write a program that removes all the occurrences of a specified string from a text file. 
Your program should prompt the user to enter a filename and a string to be removed. 
 """   
 
infile = input("enter a filename: ")
del_str = input ("Enter the string to be removed: ")
with open(infile, 'r') as f:
    file=f.read()
    while del_str in file:
        file=file.replace(del_str, '')
with open(infile, "w") as f:
    f.write(file)
    print("Done")

