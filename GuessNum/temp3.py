# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 02:00:29 2018

@author: SCM80
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 01:39:20 2018

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

i=0

"""
一開始令i=一個絕對不等於secret的值，之後要將判斷值令給i
"""


while i!=secret:

    g=input("guess a number:")


#目的="輸入=secret"則停止，故"輸入不等於secret"則繼續
#所以輸入值必須=條件，也就是i

    i=int(g)

    if i==secret:
        print("you win")
    elif i>secret:
        print("so bigger")
    else: print("so smaller")

"""這時候他會回過頭去，把i跟secret比，
但因為i這時候是你輸入的值，就看你有沒有猜對
"""

print("game over")





#import pylab

#pylab.plot(range(10),'o')

