# Five mini programming projects for the Python beginner
# https://knightlab.northwestern.edu/2014/06/05/five-mini-programming-projects-for-the-python-beginner/
# 2 of 5: Guessing Game


import random

computer=random.randint(1,10)
guess=input ("Guess the number: ")
guess=int(guess)

while guess!=computer:
    guess=input ("Guess again: ")
    guess=int(guess)    
else:
    print ("computer guess:",computer)
    print ("your guess:",guess)
