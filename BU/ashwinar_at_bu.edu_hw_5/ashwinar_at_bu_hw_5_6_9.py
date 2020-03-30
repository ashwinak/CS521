#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 02:01:49 2019

@author: ashwinak

(Conversions between feet and meters) 

Write a module that contains the following two functions:

# Converts from feet to meters
def footToMeter(foot):

# Converts from meters to feet
def meterToFoot(meter):

The formulas for the conversion are:
    
foot = meter / 0.305 
meter = 0.305 * foot

Write a test program that invokes these functions to display the following tables:
    
Feet       Meters  |  Meters  Feet  
          
1.0        0.305   |  20.0    66.574
2.0        0.610   |  26.0    81.967
                   |     
...                |  
9.0        2.745   | 60.0    196.721 
10.0       3.050   | 66.0    213.115        

"""

def footToMeter(foot):
    meter = 0.305 * foot
    return meter
    
def meterToFoot(meter):
    foot = meter / 0.305
    return foot

#print("Feet" "\t" " Meters")
#print("\t")

ftm1 = [f for f in range(1,11,1)]
ftm1 = list(map(float, ftm1))
ftm2 = []
i=1
while i<=10:
    #print(float(i),"\t",'{:.3f}'.format(footToMeter(i)))
    m = ('{:.3f}'.format(footToMeter(i)))
    ftm2.append(m)
    i+=1
#print(ftm2)
#ftm2 = list(map(float, ftm2))    
#print("")
#print("Meters" "\t" " Feet")
#print("")

mtf1 = [m for m in range(20,76,6)]
mtf1 = list(map(float, mtf1))
mtf2 = []
k=20
while k<=76:
    #print(float(k),"\t",'{:.3f}'.format(meterToFoot(k)))
    f = ('{:.3f}'.format(meterToFoot(k)))
    mtf2.append(f)
    k+=6
#mtf2 = list(map(float, mtf2))        
print("")

print("Feet\t","Meters"," | Meters", "\t Feet")
print("\t\t |")
[print("{} \t {} \t | {} \t {}".format(*row)) for row in zip(ftm1,ftm2,mtf1,mtf2)]

