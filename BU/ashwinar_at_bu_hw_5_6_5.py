#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 00:09:56 2019

@author: ashwinak

(Sort three numbers) Write the following function to display three numbers in increasing order:
def displaySortedNumbers(num1, num2, num3):
Write a test program that prompts the user to enter three numbers and invokes the function to display them in increasing order. 
Here are some sample runs:
    
"""

try:
    def displaySortedNumbers(num1, num2, num3):
        list1=[num1,num2,num3]
        list1.sort()
        print ("The sorted numbers are ",' '.join(map(str, list1)))
    
    numbers = input("Enter three numbers: ").split(",")
    
    if len(numbers) == 3:
        num1,num2,num3 = numbers[0],numbers[1],numbers[2]
        displaySortedNumbers(num1, num2, num3)
    else:
        print("Enter only 3 numbers..")
    
except IndexError:
    print("Enter only 3 numbers..")