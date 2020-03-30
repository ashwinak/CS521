#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 21:53:06 2019

@author: ashwinak

(Sum the digits in an integer using recursion) 
Write a recursive function that computes the sum of the digits in an integer. 

Use the following function header:
    
def sumDigits(n):
    
For example, sumDigits(234) returns 2 + 3 + 4 = 9. Write a test program
that prompts the user to enter an integer and displays its sum.

"""

def sumDigits(n):
    if not n:
        return 0
    return n[0] + sumDigits(n[1:])
number = (input("Enter an integer: "))
list1 = list(number)
list1 = list(map(int, list1))
print("The sum of digits in the number",number,"is", sumDigits(list1))
