# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 22:42:21 2018

@author: SCM80
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 02:05:54 2018

@author: SCM80
"""

#import可以搬到迴圈外
import urllib.request
import time

boss=4.74
price=10
sleep_min=0.1

while price>boss:
    #page=urllib.request.urlopen("http://beans-r-us.appspot.com/prices.html")
    page=urllib.request.urlopen("http://beans-r-us.appspot.com/prices-loyalty.html")
    time.sleep(sleep_min*60)
    
    text=page.read().decode("utf8")    
    #print(text)

    #price2_01=text.find("<strong>$")
    #price2_01=text.find(">$")    
    price2_01=text.find("$")
    print(price2_01)
    
    price2_02=text.find("</strong>")
    print(price2_02)
    
    price2=text[price2_01+1:price2_02]
    print(price2)
    price=float(price2)

    
    if price <= boss:
        print("Hello, Boss! Price is lower than "+str(boss)+".","Plz BUY it!")
    else:
        print(str(price)+" So bigger. plz recheck.")
        #這時候price被填入一個新的數字(當前價格)，
        #再用這個去跟boss=4.74做比較，來決定while是否運行