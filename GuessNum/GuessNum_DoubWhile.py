# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 02:01:18 2018

@author: SCM80
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
n="N"
j="A"
while j!=n:
    
    from random import randint
    secret=randint(1,10)

    
    print("\n\n\nwelcome!")
    
    """
    一開始令i=一個絕對不等於secret的值，之後要將判斷值令給i
    """
    i=0
    
    while i!=secret:
        g=input("guess a number:")
            #目的="輸入=secret"則停止，故"輸入不等於secret"則繼續
            #所以輸入值必須=條件，也就是i
        i=int(g)
    
        if i==secret:
            print("You Win!")
        elif i>secret:
            print("so bigger")
        else: print("so smaller")
        #這時候他會回過頭去，把i跟secret比，
        #但因為i這時候是你輸入的值，就看你有沒有猜對
    
    #    print("game over")
    ans=input("continue this game? Y/N")
    j=ans

    if j=="N":
        print("GameOver!")
    elif j=="Y":
        print("Try again, Good Luck!")
    else: print("plz input Y/N")

    #這時候他會回過頭去，把j跟"N"比
    #如果j不是N(也就是你輸入Y=想再玩)那他就會繼續跑while
#ans=input("continue this game? Y/N")



#import pylab

#pylab.plot(range(10),'o')

