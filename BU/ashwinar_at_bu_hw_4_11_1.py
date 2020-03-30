#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 00:08:23 2019

@author: ashwinak

(Sum elements column by column) 

Write a function that returns the sum of all the elements in a specified column in a matrix using the following header:
def sumColumn(m, columnIndex):
Write a test program that reads a 3 * 4 matrix and displays the sum of each column. Here is a sample run:

Enter a 3-by-4 matrix row for row 0: 1.5 2 3 4
Enter a 3-by-4 matrix row for row 1: 5.5 6 7 8
Enter a 3-by-4 matrix row for row 2: 9.5 1 3 1
Sum of the elements for column 0 is 16.5
Sum of the elements for column 1 is 9.0
Sum of the elements for column 2 is 13.0
Sum of the elements for column 3 is 13.0

"""

def sumColumn(m, columnIndex):
    try:
        import sys
        row0 = input("Enter a 3-by-4 matrix row for row 0: ").split(" ")
        if len(row0) != 4:
            sys.exit()
        row1 = input("Enter a 3-by-4 matrix row for row 1: ").split(" ")
        if len(row1) != 4:
            sys.exit()
        row2 = input("Enter a 3-by-4 matrix row for row 2: ").split(" ")
        if len(row2) != 4:
            sys.exit()
        row0 = list(map(float, row0))
        row1 = list(map(float, row1))
        row2 = list(map(float, row2))
        if m ==0 and columnIndex==0:
            sum0 = row0[0] + row1[0] + row2[0]
            print("")
            print("Sum of the elements for column 0 is",sum0)
            sum1 = row0[1] + row1[1] + row2[1]
            print("Sum of the elements for column 1 is",sum1)
            sum2 = row0[2] + row1[2] + row2[2]
            print("Sum of the elements for column 2 is",sum2)
            sum3 = row0[3] + row1[3] + row2[3]
            print("Sum of the elements for column 3 is",sum3)
    except IndexError:
        print("Enter the correct matrix of numbers")
    except ValueError:
        print("Enter only integers")
    except SystemExit:
        print("Enter a row with 4 colums seperated by space")
sumColumn(0,0)        

        
    
    
    
    
