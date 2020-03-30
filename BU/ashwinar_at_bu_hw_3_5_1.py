#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 22:05:38 2019

@author: ashwinak

(Count positive and negative numbers and compute the average of numbers).
Write a program that reads an unspecified number of integers, determines how many positive and negative values have been read, 
and computes the total and average of the input values (not counting zeros). 
Your program ends with the input 0. Display the average as a floating-point number.


"""
number_list = []
positive_number = []
negative_number = []                      
integer = eval(input("Enter an integer, the input ends if it is 0: "))
if integer == 0:
     print("You didn't enter any number")
else:
    while integer !=0:
        number_list.append(integer)
        integer = eval(input("Enter an integer, the input ends if it is 0: "))
    for n in number_list:
        if n > 0:
            positive_number.append(n)
        else:
            negative_number.append(n)
    print("The number of positives:",  len(positive_number))
    print("The number of negatives:", len(negative_number))
    print("The total is:", sum(number_list))
    print("The average is:", sum(number_list)/len(number_list))
