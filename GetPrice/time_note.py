# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 13:00:30 2018

@author: SCM80
"""


import time

#help(time.daylight)

print("當前時間(秒數/浮點數)=",time.clock()) 
print("UTC日期與時間(無關時區)",time.gmtime()) 
print("本地時區時間=",time.localtime()) #本地時間(有時區
print("自1970年1/1起經過之秒數=",time.time()) 

#一開始以為在這裡突然運算變慢
#結果是因為，10秒不能做事，同一串指令的print也要10秒後執行
print("幾秒內什麼都不做=",time.sleep(3))

#注意不能加()
a=time.timezone
print("你的時區 VS UTC倫敦時區的秒數差=",a)
print("你的時區 VS UTC倫敦時區的秒數差=",time.timezone) 


print("-----------我是分隔線-------------")

#這裡報錯
b=time.daylight()
print("如果目前是日光節約時間就=0,=",b)
#print("如果目前是日光節約時間就=0,=",time.daylight())


