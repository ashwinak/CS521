#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 01:17:36 2019

@author: ashwinak

Student 0 's correct count is 7
Student 1 's correct count is 6
Student 2 's correct count is 5
Student 3 's correct count is 4
Student 4 's correct count is 8
Student 5 's correct count is 7
Student 6 's correct count is 7
Student 7 's correct count is 7

Show as,
Student 3 's correct count is 4
Student 2 's correct count is 5
Student 1 's correct count is 6
Student 0 's correct count is 7
Student 5 's correct count is 7
Student 6 's correct count is 7
Student 7 's correct count is 7
Student 4 's correct count is 8
"""    
def main():
#Students' answers to the questions
    import operator
    answers = [
            ['A', 'B', 'A', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],
            ['D', 'B', 'A', 'B', 'C', 'A', 'E', 'E', 'A', 'D'],
            ['E', 'D', 'D', 'A', 'C', 'B', 'E', 'E', 'A', 'D'],
            ['C', 'B', 'A', 'E', 'D', 'C', 'E', 'E', 'A', 'D'],
            ['A', 'B', 'D', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],
            ['B', 'B', 'E', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],
            ['B', 'B', 'A', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],
            ['E', 'B', 'E', 'C', 'C', 'D', 'E', 'E', 'A', 'D']]
# Key to the questions
    keys = ['D', 'B', 'D', 'C', 'C', 'D', 'A', 'E', 'A', 'D']
    # Grade all answers
    dict ={}
    for i in range(len(answers)):
         correctCount = 0
         for j in range(len(answers[i])):
             if answers[i][j] == keys[j]:
                 correctCount += 1
         #print("Student", i, "'s correct count is", correctCount)
         dict[i] = (correctCount)
    sorted_dict = sorted(dict.items(),key=operator.itemgetter(1),reverse=False)
    for k,v in sorted_dict:
        print("Student", k, "'s correct count is", v)
main()