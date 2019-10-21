#Guessing Game

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