#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 12:59:42 2019

@author: ashwinak

(Algebra: 2 * 2 linear equations) 

Design a class named LinearEquation for a 2 * 2 system of linear equations:
    
ax+by=e x= ed-bf y= af-ec cx + dy = f ad - bc ad - bc
The class contains:
    
■ The private data fields a, b, c, d, e, and f with get methods.
■ A constructor with the arguments for a, b, c, d, e, and f.
■ Six get methods for a, b, c, d, e, and f.
■ A method named isSolvable() that returns true if ad - bc is not 0.
■ The methods getX() and getY() that return the solution for the equation.


"""
try:
    import sys
    class LinearEquation:
        def __init__(self,a=0,b=0,c=0,d=0,e=0,f=0):
            self.__a = a
            self.__b = b
            self.__c = c
            self.__d = d
            self.__e = e
            self.__f = f
        
        def getX(self):
            x = (self.__e * self.__d)-(self.__b * self.__f) / (self.__a * self.__d)-(self.__b * self.__c)
            return x
            
        def getY(self):
            y = (self.__a * self.__f) - (self.__e * self.__c) / (self.__a * self.__d ) - (self.__b * self.__c)
            return y
            
        def getA(self):
            return self.__a
    
        def getB(self):
            return self.__b
    
        def getC(self):
            return self.__c
    
        def getD(self):
            return self.__d
    
        def getE(self):
            return self.__e
    
        def getF(self):
            return self.__f
    
    
        def isSolvable(self):
            if (self.__a * self.__d)-(self.__b * self.__c) != 0:
                return True
            else:
                return False
            return
    
            
    user_input = []
    user_input = eval(input("Enter 6 numbers for (a,b,c,d,e,f) seperated by comma: "))
    #print(user_input[3])
    
    A = LinearEquation(user_input[0],user_input[1],user_input[2],user_input[3],user_input[4],user_input[5])
    
    if A.isSolvable() == True:
        print("The equation is Solvable")
    else:
        sys.exit()
        
    
#    print("A is ",A.getA())    
#    print("B is ",A.getB())
#    print("C is ",A.getC())    
#    print("D is ",A.getD())
#    print("E is ",A.getE())    
#    print("F is ",A.getF())
#    
    
    
    
    print("x is",round(A.getX(),3))
    print("y is ",round(A.getY(),3))
except SystemExit:
    print("The equation has no solution")

