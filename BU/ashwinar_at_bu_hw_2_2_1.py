#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 08:17:36 2019

@author: ashwinak

(Convert Celsius to Fahrenheit) 
Write a program that reads a Celsius degree from the 
console and converts it to Fahrenheit and displays the result. 
The formula for the conversion is as follows: fahrenheit = (9 / 5) * celsius + 32
      
"""

celsius = eval(input ("Enter a degree in celsius:"))
#print(type(celsius))
fahrenheit = round((9 / 5) * celsius + 32,3)
#fahrenheit = (9 / 5) * celsius + 32
print (celsius, "Celsius is", fahrenheit, "Fahrenheit")
