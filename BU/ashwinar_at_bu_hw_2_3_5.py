#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 00:33:13 2019

@author: ashwinak

(Geometry: area of a regular polygon) 
A regular polygon is an n-sided polygon in which all sides are of the same length and all angles have the same degree 
(i.e., the polygon is both equilateral and equiangular). 
The formula for computing the area of a regular polygon is
Area =  n * s ** 2/4 * tan (pi/n)
Here, s is the length of a side. Write a program that prompts the user to enter the number of sides and their length of a regular polygon 
and displays its area.

"""
import math
noOfSides = eval(input("Enter the number of sides: "))
lenghtOfaSide = eval(input("Enter lenght of a side: "))

areaOfPolygon = (noOfSides * (lenghtOfaSide ** 2))/(4 * math.tan(math.pi/noOfSides))
print ("The area of the polygon is " ,round(areaOfPolygon,2))



