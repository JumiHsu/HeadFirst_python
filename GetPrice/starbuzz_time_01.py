# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 02:05:54 2018

@author: SCM80
"""

#import可以搬到迴圈外
import urllib.request
boss=4.74
price=10



while price>boss:
    #page=urllib.request.urlopen("http://beans-r-us.appspot.com/prices.html")
    page=urllib.request.urlopen("http://beans-r-us.appspot.com/prices-loyalty.html")
    
    text=page.read().decode("utf8")    
    #print(text)
    
    #price0=text[233:238]
    #print(price0)
    #price1=text[234:238]
    #print(price1)
    
    price2_01=text.find("$")
    #price2_01=text.find("<strong>$")
    #price2_01=text.find(">$")
    print(price2_01)
    
    price2_02=text.find("</strong>")
    print(price2_02)
    
    price2=text[price2_01+1:price2_02]
    print(price2)
    price=float(price2)

    
    if price <= boss:
        print("Hello! Boss! Price is lower than "+str(boss))
    else:
        print(str(price)+" So bigger. plz recheck.")
        #這時候price被填入一個新的數字(當前價格)，
        #再用這個去跟boss=4.74做比較，來決定while是否運行