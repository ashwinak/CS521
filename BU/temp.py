#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 19:12:06 2019

@author: ashwinak

"""  
##import math
##radius = -20
##if radius >= 0:
##    area = radius * radius * math.pi
##    print("The area is", area)
##
##
##
##i=1
##while i < 10:
##	if i % 2 == 0: 
##		print(i)
##	i += 1
##    
##print("")    
##i=1
##while i < 10:
##    if i % 2 == 0: 
##        print(i)
##   i += 1    
##    
##
##    
##for i in range(1, 5): 
##    j=0
##    while j < i:
##        print(j, end = " ") 
##        j += 1
##      
###i=0
###while i < 5:
###    for j in range(i, 1, -1): 
###        print(j, end = " ")
###        print("****") 
###    i += 1        
###    
#    
##balance = 1000 
##while True:
##    if balance < 9: 
##        continue
##    balance = balance - 9 
##print("Balance is", balance)
##    
#
#i=0
#while i < 4:
#    if i % 3 == 0:
#        continue
#    sum += i 
#    i += 1
#



# Create a list of 99 Boolean elements with value False 2 
#
#isCovered = 20 * [False]
##print("first", isCovered)
#endOfInput = False
#while not endOfInput:
## Read numbers as a string from the console
#    s = input("Enter a line of numbers separated by spaces: ") 
#    items = s.split() # Extract items from the string
#    lst = [eval(x) for x in items] # Convert items to numbers get input numbers 9
##    print("list",lst)
#    for number in lst:
#        if number == 0:
#            endOfInput = True
#        else:
#            isCovered[number - 1] = True
#allCovered = True # Assume all covered initially
#for i in range(20):
#    if not isCovered[i]:
#        allCovered = False # Find one number not covered break
#print(isCovered)
## Display result
#if allCovered:
#    print("The tickets cover all numbers")
#else:
#    print("The tickets don't cover all numbers")



matrix = [] # Create an empty list
numberOfRows = 3
numberOfColumns = 3
#numberOfRows = eval(input("Enter the number of rows: ")) 
#numberOfColumns = eval(input("Enter the number of columns: ")) 
for row in range(numberOfRows):
    matrix.append([]) # Add an empty new row 
    for column in range(numberOfColumns):
        value = eval(input("Enter an element and press Enter: ")) 
        matrix[row].append(value)
print("matrix is", matrix)

