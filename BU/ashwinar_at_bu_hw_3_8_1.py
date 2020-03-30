#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 21:29:22 2019

@author: ashwinak

(Check SSN) 
Write a program that prompts the user to enter a Social Security number in the format ddd-dd-dddd, 
where d is a digit. The program displays Valid SSN for a correct Social Security number or Invalid SSN otherwise.


123-45-7890
123-45-abcd
abc-45-7890
abc-de-fghi
12-345-6780

"""

import sys
SSN = input("Enter the SSN number: ")
ssn_list = list(SSN)
try:
    for characters in ssn_list:
        if any(characters.isalpha() for char in characters):
            sys.exit()
    if (len(ssn_list) == 11 and ssn_list[3] == "-" and  ssn_list[6] == "-"):
        print("Valid SSN number")
    else:
        print("Invalid SSN number")
except IndexError:
    print("Invalid SSN number")
except SystemExit:
    print("Invalid SSN number")
                

