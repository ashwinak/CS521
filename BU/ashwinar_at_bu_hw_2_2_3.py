#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 19:46:48 2019

@author: ashwinak

(Convert feet into meters) 
Write a program that reads a number in feet, converts it to meters, 
and displays the result. One foot is 0.305 meters.

"""

feet = eval(input("Enter a number in feet: "))
meter= round(feet * 0.305,3)
print(feet, "feet is" , meter, "meters")
