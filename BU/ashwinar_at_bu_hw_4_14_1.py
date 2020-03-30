#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 17:27:15 2019

@author: ashwinak

(Display keywords) Revise Listing 14.4 CountKeywords.py to display the keywords in a Python source file 
as well as to count the number of the keywords.

"""

import os.path
import sys

def main():
    try:
        keyWords = {"and", "as", "assert", "break", "class",
                    "continue", "def", "del", "elif", "else",
                    "except", "False", "finally", "for", "from",
                    "global", "if", "import", "in", "is", "lambda",
                    "None", "nonlocal", "not", "or", "pass", "raise",
                     "return", "True", "try", "while", "with", "yield"}
    
        filename = input("Enter a Python source code filename: ").strip()
        if not os.path.isfile(filename): # Check if file exists
            #print("File", filename, "does not exist")
            sys.exit()
        infile = open(filename, "r") # Open files for input
        text = infile.read().split() # Read and split words from the file 21
        count = 0
        for word in text:
            if word in keyWords:
                count += 1
                print("The keyword found in file", filename,"is", word)
        print("The number of keywords in", filename, "is", count)
    except SystemExit:
        print("File", filename, "does not exist")
main()


