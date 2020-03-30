#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 21:59:00 2019

@author: ashwinak
"""

import math
def circle_area(r):
    area = math.pi * r**2 
    return area
radius = eval(input("radius: "))
#radius = 10
if isinstance(radius, (int, float)):
    area = round(circle_area(radius), 2)
    print("area: " + str(area)) 
else:
    print(radius, " is non-numeric!!!")
    
    
    