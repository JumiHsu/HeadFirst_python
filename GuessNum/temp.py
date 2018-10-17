# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from random import randint
secret=randint(1,10)

print("\n\n\nwelcome!")

i=0
#ans=input("continue this game? Y/N?")

while i!=1:

    g=input("guess a number:")
    guess=int(g)

    if guess==secret:
        print("you win")
    elif guess>secret:
        print("so bigger")

    else: print("so smaller")


print("game over")




