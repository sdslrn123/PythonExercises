# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 18:20:30 2019

@author: syeds
"""

#DiceSimulator

import random

#input ("Would you like to roll the dice?(Y/N) ")
decision=input ("Would you like to roll the dice?(Y/N) ")
#print (decision)
while decision == ("Y"):
        result=random.randint(1,6)
        print (result)
        decision=input ("Would you like to roll the dice again?(Y/N) ")
else:
    print ("Game Over")
