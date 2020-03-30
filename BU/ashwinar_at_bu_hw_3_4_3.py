#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 00:39:53 2019

@author: ashwinak

(Algebra: solve 2 * 2 linear equations) You can use Cramer’s rule to solve the following 2 * 2 system of linear equation:

ax + by = e
cx + dy = f
x= ed-bf/ad - bc 
y= af-ec/ad - bc  

Write a program that prompts the user to enter a, b, c, d, e, and f and display the result. 
If ad – bc is 0, report that The equation has no solution.
    
"""

try:
    a,b,c,d,e,f = eval(input("Enter a,b,c,d,e,f: "))
    x= (e * d- b* f)/(a * d - b * c) 
    y= (a * f-e * c)/(a * d - b * c)
    #if (a * (d - b) * c) == 0:
    print ("x is " ,x , "and y is",y)
except ZeroDivisionError:
    print("The equation has no solution")
    
