#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 18:23:44 2019

@author: ashwinak
"""

class GeometricObject:
	def __init__(self, color = "green", filled = True):
		self.__color = color
		self.__filled = filled
		
	def getColor(self):
		return self.__color
    	
	def setColor(self,color):
		self.__color = color
	
	def isFilled(self):
		return self.__filled
		
	def setFilled(self,filled):
		self.__filled = filled
	
	def __str__(self):
		return "color: " + self.__color + " and filled: " + str(self.__filled)