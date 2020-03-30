#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  8 00:26:21 2019

@author: ashwinak

(Geography: estimate areas) 
Find the GPS locations for Atlanta, Georgia; Orlando, Florida; Savannah, Georgia; and Charlotte, North Carolina 
from www.gps-data-team.com/map/ and compute the estimated area enclosed by these four cities. 
(Hint: Use the formula in Programming Exercise 3.2 to compute the distance between two cities. 
Divide the polygon into two triangles and use the formula in Programming Exercise 2.14 to compute the area of a triangle.)

d = radius * arccos(sin(x1) * sin(x2) + cos(x1) * cos(x2) * cos(y1 - y2))

The average earth radius is 6,371.01 km
Decimal coordinates (latitude, longitude):
    
Atlanta, Georgia:  33.7405800,-84.5545400
Charlotte, North Carolina: 35.2072400,-80.9567600
Savannah, Georgia: 32.1672300,-81.1998900
Orlando, Florida: 28.4115300,-81.5250400

x1,y1 = math.radians(39.55), math.radians(-116.25)
x2,y2 = math.radians(41.5), math.radians(87.37)
radius=6371.01
d = radius * acos(sin(x1) * sin(x2) + cos(x1) * cos(x2) * cos(y1 - y2))

(Geometry: area of a triangle) 
Write a program that prompts the user to enter the three points (x1, y1), (x2, y2), 
and (x3, y3) of a triangle and displays its area. The formula for computing the area of a triangle is
s = (side1 + side2 + side3)/2

area = sqrt(s(s - side1)(s - side2)(s - side3))


"""

from math import radians,acos,cos,sin, sqrt
alat,alon = radians(33.7405800),radians(-84.5545400)
clat,clon = radians(35.2072400),radians(-80.9567600)
slat,slon = radians(32.1672300),radians(-81.1998900)
olat,olon = radians(28.4115300),radians(-81.5250400)
radius = 6371.01

#Triangle 1 (Atl-Cha-Sav-Atl) Length of all 3 sides of a triangle.
d_Atl_Cha = radius * acos(sin(alat) * sin(clat) + cos(alat) * cos(clat) * cos(alon - clon))
d_Cha_Sav = radius * acos(sin(clat) * sin(slat) + cos(clat) * cos(slat) * cos(clon - slon))
d_Sav_Atl = radius * acos(sin(slat) * sin(alat) + cos(slat) * cos(alat) * cos(slon - alon))

s1 = (d_Atl_Cha + d_Cha_Sav + d_Sav_Atl)/2
areaOfTriangle1 = sqrt(s1 * (s1-d_Atl_Cha) * (s1-d_Cha_Sav) * (s1-d_Sav_Atl))
print("Area of Triangle 1 [Atlanta,Charlotte,Savannah,Atlanta] is, " ,round(areaOfTriangle1,3), "kms" )

#Triangle 2 (Atl-Sav-Orl-Atl) Length of all 3 sides of a triangle.
d_Atl_Sav = radius * acos(sin(alat) * sin(slat) + cos(alat) * cos(slat) * cos(alon - slon))
d_Sav_Orl = radius * acos(sin(slat) * sin(olat) + cos(slat) * cos(olat) * cos(slon - olon))
d_Orl_Atl = radius * acos(sin(olat) * sin(alat) + cos(olat) * cos(alat) * cos(olon - alon))

s2 = (d_Atl_Sav + d_Sav_Orl + d_Orl_Atl)/2
areaOfTriangle2 = sqrt(s2 * (s2-d_Atl_Sav) * (s2-d_Sav_Orl) * (s2-d_Orl_Atl))
print("Area of Triangle 2 [Atlanta,Savannah,Orlando,Atlanta] is, " ,round(areaOfTriangle2,3), "kms" )
print("Total area of Atlanta,Charlotte,Savannah,Orlando is" , round(areaOfTriangle1 + areaOfTriangle2,3), "kms")



