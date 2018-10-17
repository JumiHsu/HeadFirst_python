# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 01:51:41 2018

@author: SCM80
"""


#import可以搬到迴圈外
import urllib.request
import time

boss=4.74
price=10.0
sleep_min=0.05

#取得目標網頁的價格資訊
#需要import time

#page=urllib.request.urlopen("http://beans-r-us.appspot.com/prices.html")
page=urllib.request.urlopen("http://beans-r-us.appspot.com/prices-loyalty.html")
time.sleep(sleep_min*60)

text=page.read().decode("utf8")    

#price2_01=text.find("<strong>$")
#price2_01=text.find(">$")    
price2_01=text.find("$")
#    print(price2_01)    
price2_02=text.find("</strong>")
#    print(price2_02)

price_str=text[price2_01+1:price2_02]
price=float(price_str)
print(price)
