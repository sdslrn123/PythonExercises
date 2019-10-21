# DiceSimulator
# https://knightlab.northwestern.edu/2014/06/05/five-mini-programming-projects-for-the-python-beginner/

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
