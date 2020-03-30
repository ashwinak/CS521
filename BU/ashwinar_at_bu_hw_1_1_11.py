#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 27 18:37:24 2019

@author: ashwinak
"""

'''
One birth every 7 seconds.
One death every 13 seconds.
One new immigrant every 45 seconds.

Write code to display the population of each of the next five years.

Assume current population is 312032486
one year = 365 days.
hint : use division operator //
'''

currentPopulation=312032486

birthPerYear = 365 * 24 * 3600 // 7
deathPerYear = 365 * 24 * 3600 // 13
newImmigrantPerYear = 365 * 24 * 3600 // 45

populationAfterOneYear = currentPopulation + (1 * birthPerYear) - (1 * deathPerYear) + ( 1 * newImmigrantPerYear)
populationAfterTwoYears = currentPopulation + (2 * birthPerYear) - (2 * deathPerYear) + ( 2 * newImmigrantPerYear)
populationAfterThreeYears = currentPopulation + (3 * birthPerYear) - (3 * deathPerYear) + ( 3 * newImmigrantPerYear)
populationAfterFourYears = currentPopulation + (4 * birthPerYear) - (4 * deathPerYear) + ( 4 * newImmigrantPerYear)
populationAfterFiveYears = currentPopulation + (5 * birthPerYear) - (5 * deathPerYear) + ( 5 * newImmigrantPerYear)

print ("Population after 1 year is",populationAfterOneYear, \
      "\nPopulation after 2 years is",populationAfterTwoYears, \
      "\nPopulation after 3 years is",populationAfterThreeYears, \
      "\nPopulation after 4 years is",populationAfterFourYears, \
      "\nPopulation after 5 years is",populationAfterFiveYears)


