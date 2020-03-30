#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 11:09:06 2019

@author: ashwinak
"""

deck = [x for x in range(52)]
suits = ["Spades", "Hearts", "Diamonds", "Clubs"]
ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10","Jack,","Queen", "King"]
import random
random.shuffle(deck)
print(deck)
for i in range(4):
    print("i is",i)
    suit = suits[deck[i] // 13]
    rank = ranks[deck[i] % 13]
    print("Card number", deck[i], "is the", rank, "of", suit)



