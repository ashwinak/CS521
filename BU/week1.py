#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 26 19:36:07 2019

@author: ashwinak
"""

x = "hello"
y = "hello"

print(id(x))
#print(id(y))

print(hash(x))
print(hash(y))

#radius = eval(input("Enter a radius: "))


import time
currentTime = time.time()
# Obtain the total seconds since midnight, Jan 1, 1970 6 
totalSeconds = int(currentTime)
# Get the current second
currentSecond = totalSeconds % 60
# Obtain the total minutes
totalMinutes = totalSeconds // 60
# Compute the current minute in the hour 15 
currentMinute = totalMinutes % 60
# Obtain the total hours
totalHours = totalMinutes // 60
# Compute the current hour
currentHour = totalHours % 24
time.time()
# Display results
print ('''
       
       ''')
print("Current time is", currentHour,":",currentMinute,":", currentSecond, "GMT")

a=1
a,b=a+1,a+2
print(a,b)


print("Enter three numbers: ")
number1 = eval(input())
number2 = eval(input())
number3 = eval(input())

 # Compute average
average = (number1 + number2 + number3) / 3
print(average)


