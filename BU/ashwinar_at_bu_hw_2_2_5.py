#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 20:40:00 2019

@author: ashwinak

(Financial application: calculate tips) 
Write a program that reads the subtotal and the gratuity rate and computes the gratuity and total. 
For example, if the user enters 10 for the subtotal and 15% for the gratuity rate, 
the program displays 1.5 as the gratuity and 11.5 as the total

"""

subTotal,gratuityRate = eval(input("Enter the subtotal and a gratuity rate: "))

gratuity= round((subTotal/100) * gratuityRate, 2)

total= round(subTotal + gratuity , 2)

print("The gratuity is ",gratuity, "and the total is ", total)





