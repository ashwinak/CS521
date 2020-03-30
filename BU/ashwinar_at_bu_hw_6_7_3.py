#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 18:32:04 2019

@author: ashwinak

(The Account class) 

Design a class named Account that contains:
    
■ A private int data field named id for the account.
■ A private float data field named balance for the account.
■ A private float data field named annualInterestRate that stores the current
interest rate.
■ A constructor that creates an account with the specified id (default 0), initial
balance (default 100), and annual interest rate (default 0).
■ The accessor and mutator methods for id, balance, and annualInterestRate.


■ A method named getMonthlyInterestRate() that returns the monthly
interest rate.
■ A method named getMonthlyInterest() that returns the monthly interest.
■ A method named withdraw that withdraws a specified amount from the
account.
■ A method named deposit that deposits a specified amount to the account.


"""

class Account:
    def __init__(self,id=0,balance=100.0,annual_interest_rate=0.0):
        self.__id= id
        self.__balance = balance
        self.__annual_interest_rate = annual_interest_rate
        
    def getID(self):
        return self.__id
    
    def setID(self,id):
        self.__id = id

    def getBalance(self):
        return self.__balance

    def setBalance(self,balance):
        self.__balance = balance

    def getAnnual_Interest_Rate(self):
        return self.__annual_interest_rate

    def setAnnual_Interest_Rate(self,annual_interest_rate):
        self.__annual_interest_rate = annual_interest_rate
    
    
    def getMonthlyInterestRate(self):
        MonthlyInterestRate = self.__annual_interest_rate / 12
        return MonthlyInterestRate
        
    def getMonthlyInterest(self):
        MonthlyInterest = (self.__annual_interest_rate / 1200) * self.__balance
        return MonthlyInterest
        
    def withdraw(self,withdraw):
        self.__balance = self.__balance - withdraw
                
    def deposit(self,deposit):
        self.__balance = self.__balance + deposit

A = Account(10,1000.10,2.09)


A.setID(1122)
A.setBalance(20000)
A.setAnnual_Interest_Rate(4.5)
A.withdraw(2500)
A.deposit(3000)

print("The ID of user A is",A.getID())
print("The Balance for user A is",A.getBalance(),"$")
print("The monthly interest rate for user A is",A.getMonthlyInterestRate(),"%")
print("The monthly interest for user A is ",A.getMonthlyInterest(),"$")


#print("The ID for Account A is", A.getID())
#
#print("The Annual interest rate for Account A",A.getAnnual_Interest_Rate())
#
#A.deposit(200)
#print("The remaining balance for Account A is ",A.getBalance())
#
#A.withdraw(100)
#print("The remaining balance for Account A is ",A.getBalance())
#
#print("Monthly interest rate for  Account A is",round(A.getMonthlyInterestRate(),3))
#
#print("Monthly interest for  Account A is",round(A.getMonthlyInterest(),3))
#
#
#A.setID(15)
#
#print("The ID for Account A is", A.getID())
#
#A.setBalance(1500)
#
#print("The remaining balance for Account A is ",A.getBalance())
#
#A.setAnnual_Interest_Rate(5.09)
#
#print("The Annual interest rate for Account A",A.getAnnual_Interest_Rate())










