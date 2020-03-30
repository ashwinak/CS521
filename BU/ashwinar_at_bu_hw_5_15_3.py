#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 01:03:10 2019

@author: ashwinak

(Compute greatest common divisor using recursion) 

The gcd(m, n) can also be defined recursively as follows:
■ If m % n is 0,gcd(m, n)is n.

■ Otherwise,gcd(m, n)is gcd(n, m % n).

Write a recursive function to find the GCD. Write a test program that prompts the user to enter two integers and displays their GCD.

"""

def gcd(m,n):
    d = m % n
    if d == 0:
        return n
    elif d == 1:
        return 1
    return gcd(n,d)

a,b = eval(input("Enter two numbers to find GCD: "))
print(gcd(a,b))
