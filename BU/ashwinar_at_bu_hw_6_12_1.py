#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 16:29:56 2019

@author: ashwinak

(The Triangle class) 

Design a class named Triangle that extends the GeometricObject class. The Triangle class contains:
    
■ Three float data fields named side1, side2, and side3 to denote the three sides of the triangle.
■ A constructor that creates a triangle with the specified side1, side2, and side3 with default values 1.0.
■ The accessor methods for all three data fields.
■ A method named getArea() that returns the area of this triangle.
■ A method named getPerimeter() that returns the perimeter of this triangle.
■ A method named _ _str_ _() that returns a string description for the triangle.

For the formula to compute the area of a triangle, see Exercise 2.14. The
_ _str_ _() method is implemented as follows:
return "Triangle: side1 = " + str(side1) + " side2 = " +
str(side2) + " side3 = " + str(side3)

Area of Triangle: 
s = (side1 + side2 + side3)/2

Area = sqrt(s(s-side1)(s-side2(s-side3))


Write a test program that prompts the user to enter the three sides of the triangle, a color, and 1 or 0 to indicate whether the tri- angle is filled. 
The program should create a Triangle object with these sides and set the color and filled properties using the input. 
The program should display the triangle’s area, perimeter, color, and True or False to indicate whether the triangle is filled or not.


"""

#class GeometricObject:
#	def __init__(self, color = "green", filled = True):
#		self.__color = color
#		self.__filled = filled
#		
#	def getColor(self):
#		return self.__color
#	
#	def setColor(self,color):
#		self.__color = color
#	
#	def isFilled(self):
#		return self.__filled
#		
#	def setFilled(self,filled):
#		self.__filled = filled
#	
#	def __str__(self):
#		return "color: " + self.__color + " and filled: " + str(self.__filled)

try:
    from GeometricObject import GeometricObject
    import math
    import sys
    class Triangle(GeometricObject):
        def __init__(self,side1=1.0,side2=1.0,side3=1.0):
            super().__init__()
            self.__side1 = side1
            self.__side2 = side2
            self.__side3 = side3
        
        def getSide1(self):
            return self.__side1
        
        def getSide2(self):
            return self.__side2
        
        def getSide3(self):
            return self.__side3
        
        def getArea(self):
            s = (self.__side1 + self.__side2 + self.__side3)/2
            Area = math.sqrt(s * (s - self.__side1) * (s - self.__side2) * (s - self.__side3))
            return Area
            
        def getPerimeter(self):
            Peremeter = (self.__side1 + self.__side2 + self.__side3)
            return Peremeter
            
        def __str__(self):
            return "Triangle: side1 = " + str(self.__side1) + " side2 = " + str(self.__side2) + " side3 = " + str(self.__side3)
            
    user_input = []
    
    user_input_side = eval(input("Enter the length of three sides of a triangle seperated by comma: "))
    
    user_input_color = input("Enter a color for the triangle: ")
    
    user_input_color_fill = eval(input("Enter 0 if trangle is not filled or 1 if the triangle is filled with color : "))
    
    A = Triangle(user_input_side[0],user_input_side[1],user_input_side[2])
    
#    print(user_input_color.getColor())
    
    print("---")
    
    A.setColor(user_input_color)

    if (user_input_color_fill == 0):
        print("Triangle is filled with color: False")
    elif (user_input_color_fill == 1):
        print("Triangle is filled with color:",A.isFilled())
    else:
        sys.exit()

    print("Triangle color is",A.getColor())
    
    print("Area of triangle A is", round(A.getArea(),3))
    
    print("Perimeter of triangle A is",round(A.getPerimeter(),3))
    
#    print("The color of the triange is ",A.GeometricObject.getColor())

except SystemExit:
    print("Invalid input.Enter only 0 or 1 for fill color")
















