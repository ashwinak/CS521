#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 19:35:14 2019

@author: ashwinak

(Assign grades)
Write a program that reads a list of scores and then assigns grades based on the following scheme:
The grade is A if score is > = best – 10. 
The grade is B if score is > = best – 20. 
The grade is C if score is > = best – 30. 
The grade is D if score is > = best – 40. 
The grade is F otherwise.

Here is a sample run:
    
Enter scores: 40 55 70 58

Student 0 score is 40 and grade is C
Student 1 score is 55 and grade is B
Student 2 score is 70 and grade is A
Student 3 score is 58 and grade is B
   
"""
try:
    scores = input("Enter scores: ").split(" ")
    scores = list(map(int, scores))
    best = max(scores)
    index =0
    while index < len(scores):
        if scores[index] >= max(scores) - 10:
            print("Student", index, "score is",scores[index], "and grade is A")
        elif scores[index] >= max(scores) - 20:
            print("Student", index, "score is",scores[index], "and grade is B")
        elif scores[index] >= max(scores) - 30:
            print("Student", index, "score is",scores[index], "and grade is C")
        elif scores[index] >= max(scores) - 40:
            print("Student", index, "score is",scores[index], "and grade is D")
        else:
            print("Student", index, "score is",scores[index], "and grade is F")
        index+=1
except:
    print("Invalid input, Enter integer with single space")
           
        
        
        