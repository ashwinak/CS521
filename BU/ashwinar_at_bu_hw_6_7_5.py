#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 00:14:28 2019

@author: ashwinak

(Geometry: n-sided regular polygon) 
An n-sided regular polygon’s sides all have the same length and all of its angles have the same degree 
(i.e., the polygon is both equilateral and equiangular). Design a class named RegularPolygon that contains:
    
■ A private int data field named n that defines the number of sides in the polygon.
■ A private float data field named side that stores the length of the side.
■ A private float data field named x that defines the x-coordinate of the center of the polygon with default value 0.
■ A private float data field named y that defines the y-coordinate of the center of the polygon with default value 0.

■ A constructor that creates a regular polygon with the specified n (default 3), side (default 1), x (default 0), and y (default 0).
■ The accessor and mutator methods for all data fields.
■ The method getPerimeter() that returns the perimeter of the polygon.
■ The method getArea() that returns the area of the polygon. The formula for
n * s2 computing the area of a regular polygon is 

Area = p .4*tan¢ ≤ n


"""
import math
class RegularPolygon:
    def __init__(self,n=3,side=1.0,xCoordinate=0.0,yCoordinate=0.0):
        self.__n = n
        self.__side = side
        self.__xCoordinate = xCoordinate
        self.__yCoordinate = yCoordinate
        
    def getN(self):
        return self.__n
    
    def setN(self,n):
        self.__n = n

    def getSide(self):
        return self.__side
    
    def setSide(self,side):
        self.__side = side

    def getxCoordinate(self):
        return self.__xCoordinate
    
    def setxCoordinate(self,xCoordinate):
        self.__xCoordinate = xCoordinate

    def getyCoordinate(self):
        return self.__yCoordinate
    
    def setyCoordinate(self,yCoordinate):
        self.__yCoordinate = yCoordinate
        
    def getPerimeter(self):
        Perimeter = self.__n * self.__side
        return Perimeter
        
    def getArea(self):
        Area = (self.__n * (self.__side * self.__side))/ (4 * (math.tan(math.pi/self.__n)))
        return Area
    
A = RegularPolygon()

B = RegularPolygon(6,4)

C = RegularPolygon(10,4,5.6,7.8)

print("The perimeter of the regular polygon A is",round(A.getPerimeter(),3), "cm")
print("The area of the regular polygon A is",round(A.getArea(),3),"cmsq")

print("The perimeter of the regular polygon B is",round(B.getPerimeter(),3), "cm")
print("The area of the regular polygon B is",round(B.getArea(),3),"cmsq")

print("The perimeter of the regular polygon C is",round(C.getPerimeter(),3), "cm")
print("The area of the regular polygon C is",round(C.getArea(),3),"cmsq")




#print("Number of sides is",A.getN())
#
#A.setN(5)
#    
#print("Number of sides is",A.getN())
#    
#print("THe lenght of the side is",A.getSide())
#
#A.setSide(4.5)
#        
#print("THe lenght of the side is",A.getSide())
#                        
#
#print("The X-coordinate is",A.getxCoordinate())
#
#A.setxCoordinate(2.0)
#
#print("The X-coordinate is",A.getxCoordinate())
#
#
#print("The y-coordinate is",A.getyCoordinate())
#A.setyCoordinate(3.0)
#
#print("The y-coordinate is",A.getyCoordinate())
#
#print("The perimeter of the regular polygon is",round(A.getPerimeter(),3), "cm")
#
#print("The area of the regular polygon is",round(A.getArea(),3),"cmsq")
#
#
