# Five mini programming projects for the Python beginner
# https://knightlab.northwestern.edu/2014/06/05/five-mini-programming-projects-for-the-python-beginner/
# 1 of 5: Dice Simulator

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
