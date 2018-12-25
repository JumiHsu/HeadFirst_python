# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 13:00:30 2018

@author: SCM80
"""


import time

print("\n---------------- import time -------------------")
#help(time.daylight)
a=time.clock()  # time.clock() 所在行，一定會被print出來
print("\n當前時間(秒數/浮點數)=",a)
# print("\n當前時間(秒數/浮點數)=",time.clock())
# 所以如果上面這樣寫，也會整行被print出來


print("\n本地時區時間=",time.localtime()) #本地時間(有時區
print("\n自1970年1/1起經過之秒數=",time.time())


#一開始以為在這裡突然運算變慢
#結果是因為，10秒不能做事，同一串指令的print也要10秒後執行
print("\n幾秒內什麼都不做=",time.sleep(1))


print("\n---------------- UTF時區 -----------------------")

print("UTC日期與時間(無關時區)=\n",time.gmtime() ,"\n")
#注意不能加()
print("你的時區 VS UTC倫敦時區的秒數差=",time.timezone) 



print("\n---------------- 會報錯先關閉 ------------------")
'''#這裡報錯
b=time.daylight()
print("如果目前是日光節約時間就=0,=",b)
#print("如果目前是日光節約時間就=0,=",time.daylight())'''


print("\n---------------- import datetime ---------------")
import datetime

print("\n------------ 抓取當前時間/定義昨天 -------------")
print("datetime.datetime.now() =",datetime.datetime.now())

yesterday = ( datetime.datetime.now() - datetime.timedelta(days=1) )
print("yesterday =",yesterday)

yesterdayStrf = yesterday.strftime("%Y%m%d")
print("yesterday(strftime後) =",yesterdayStrf)



print("\n---------- 計算指定日期之間的天數差 ------------")
print("datetime.datetime(2018,11,20) =" ,datetime.datetime(2018,11,20))

a=datetime.datetime(2018,11,20)  # 至少一定要填到"day"他才會給你做運算
b=datetime.datetime(2018,11,19)
print("之間的日期差 =",a-b)



# 先把 "20181120" 填入到 datetime.datetime(2018,11,20)
# 再令 日期的位移值 delta = datetime.timedelta(days=1)
# (以日期格式表示)
# .strftime('%Y%m%d') = 將算出來的days，以yyyymmdd的格式表示

import json

def get_datelist(starttime,endtime):
    startdate = datetime.datetime(int(starttime[0:4]),int(starttime[4:6]),int(starttime[6:8]))
    #now = datetime.datetime.now()
    delta = datetime.timedelta(days=1)
    # my_yestoday = startdate + delta
    # my_yes_time = my_yestoday.strftime('%Y%m%d')
    n = 0
    date_list = []
    while 1:
        if starttime<=endtime:
            days = (startdate  + delta*n).strftime('%Y%m%d')
            n = n+1
            date_list.append(days)
            if days == endtime:
                break
    return date_list

start="20181124"
end="20181201"



print("\n以json方式表示：")
print("get_datelist(",start,",",end,")=")
print( json.dumps( get_datelist(start,end) ,indent=1) )
print("期間所包含的日期數 =", len( get_datelist(start,end) ) ,"天")


early = datetime.datetime(int(start[0:4]),int(start[4:6]),int(start[6:8]))
late  = datetime.datetime(int(  end[0:4]),int(  end[4:6]),int(  end[6:8]))

diff = late - early   # diff = 7 days, 0:00:00
# 留意 timedelta格式不是字串，且數字與days之間必夾一個空白

daysLocation = str(diff).find("days")
days = int(str(diff)[0: int(daysLocation) ]) # 7
print("期間共經過：", days ,"天")



print("\n---------- 列出當前日期，的前 k 天日期(包含當日) --------")
def seven_day_list(year_mon_day,n,i=0):
    '''計算當前日期的 前n天 列表，返回：2018-11-18, ... ,2018-11-20'''
    myday = datetime.datetime( int(year_mon_day[0:4]),int(year_mon_day[4:6]),int(year_mon_day[6:8]) )
    day_list = []
    for i in range(i,n):
        days = (myday + datetime.timedelta(days=-i)).strftime('%Y-%m-%d')
        day_list.append(days)
    return day_list[::-1]

print( seven_day_list("20181120",7) )






print("\n-------------- import calendar -----------------")
print("\n--- 回傳指定年月的，第一天是星期幾(一~日=0~6) + 該月份有幾天 ---")
import calendar
monthRange = calendar.monthrange(2018,11)
print("2018年11月的第一天 = 星期",monthRange[0]+1)
print("2018年11月有",monthRange[1] ,"天")




