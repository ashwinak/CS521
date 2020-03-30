#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 20:49:05 2019

@author: ashwinak

(Algebra: solve quadratic equations) The two roots of a quadratic equation, for example, 

ax2 + bx + c = 0, can be obtained using the following formula:

r1 = -b + math.sqrt(b ** 2 - 4 * a * c)/2 * a
r2 = -b - math.sqrt(b ** 2 -4 * a * c)/2 * a

    
b2 - 4ac is called the discriminant of the quadratic equation. If it is positive, the equation has two real roots. 
If it is zero, the equation has one root. If it is negative, the equation has no real roots.
Write a program that prompts the user to enter values for a, b, and c and displays the result based on the discriminant. 
If the discriminant is positive, display two roots. If the discriminant is 0, display one root. Otherwise, display The equation has no real roots.    

"""
import math

try:
    a,b,c = eval(input("Enter a,b,c: "))
    r1 = (-b + math.sqrt(b ** 2 - 4 * a * c))/2 * a
    r2 = (-b - math.sqrt(b ** 2 -4 * a * c))/2 * a
    # discriminant
    dis = b ** 2 - 4 * a * c
    if dis > 0:
        print("The roots are",round(r1,4), "and", round(r2,4))
    elif dis == 0:
        print("The root is", round(r1,4))
except ValueError:
    print("The equation has no real roots")
    