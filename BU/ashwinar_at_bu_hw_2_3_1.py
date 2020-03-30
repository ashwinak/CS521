#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 21:25:41 2019

@author: ashwinak

(Geometry: area of a pentagon) 
Write a program that prompts the user to enter the length from the center of a pentagon to a vertex 
and computes the area of the pentagon, as shown in the following figure.

The formula for computing the area of a pentagon is Area = 3 sqrt(3)/2 * s ** 2, where s is
the length of a side. The side can be computed using the formula s = 2r sin pi/5,
where r is the length from the center of a pentagon to a vertex. 

"""

import math

length_CenterToVertex = eval(input("Enter the length from the center to a vertex: "))

lenght_OfSide = (2 * length_CenterToVertex) * math.sin(math.pi/5)

areaOfPentagon = round(((3 * math.sqrt(3))/2) * lenght_OfSide ** 2,2)

print ("The area of the pentagon is: ",areaOfPentagon)


