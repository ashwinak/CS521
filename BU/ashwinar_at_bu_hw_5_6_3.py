#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 23:45:10 2019

@author: ashwinak

(Palindrome integer) 

Write the functions with the following headers:

# Return the reversal of an integer, e.g. reverse(456) returns # 654
def reverse(number):

# Return true if number is a palindrome
def isPalindrome(number):

Use the reverse function to implement isPalindrome. A number is a palindrome if its reversal is the same as itself. 
Write a test program that prompts the user to enter an integer and reports whether the integer is a palindrome.

"""

def isPalindrome(number):
    list1= list(number)
    if list1[0:] == list1[::-1]:
        return True
    else:
        return False
    
    
def reverse(number):
    list1= list(number)
    print (''.join(map(str, list1[::-1])))

number = input("Enter a number to check palindrome: ")

reverse(number)

if isPalindrome(number) == True:
    print("The number", number, "is a palindrome")
else:
    print("The number", number, "is not a palindrome")