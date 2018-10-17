# -*- coding: utf-8 -*-
"""
Created on Sun Sep 23 17:57:06 2018

@author: SCM80
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from random import randint
secret=randint(1,10)

print("\n\n\nwelcome!")

guess=0
#ans=input("continue this game? Y/N?")

while guess!=secret:

    g=input("guess a number:")
    guess=int(g)

    if guess==secret:
        print("you win")
    elif guess>secret:
        print("so bigger")

    else: print("so smaller")


print("game over")


#import pylab

#pylab.plot(range(10),'o')

