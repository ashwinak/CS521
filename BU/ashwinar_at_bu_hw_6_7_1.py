#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 17:48:59 2019

@author: ashwinak

(The Rectangle class) 

Following the example of the Circle class in Section 7.2, design a class named Rectangle to represent a rectangle. 

The class contains:
■ Two data fields named width and height.
■ A constructor that creates a rectangle with the specified width and height.

The default values are 1 and 2 for the width and height, respectively.

■ A method named getArea() that returns the area of this rectangle.
■ A method named getPerimeter() that returns the perimeter.

        
        self.width = width
        self.height = height

"""

class Rectangle:  # Construct a circle object
    def __init__(self, width = 1,height = 2):
        self.width = width
        self.height = height
    
    def getArea(self):
        return self.width * self.height
        
    def getPerimeter(self):
        return 2 * (self.width + self.height)


r1 = Rectangle(4,40)
r2 = Rectangle(3.5,35.7)


print("The width of rectangle r1 is", r1.width)
print("The height of rectangle r1 is", r1.height)
print("The area of rectangle r1 is", round(r1.getArea(),3))
print("The peremeter of rectangle r1 is", round(r1.getPerimeter(),3))

print("The width of rectangle r2 is", r2.width)
print("The height of rectangle r2 is", r2.height)
print("The area of rectangle r2 is", round(r2.getArea(),3))
print("The peremeter of rectangle r2 is", round(r2.getPerimeter(),3))