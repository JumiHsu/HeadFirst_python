# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 19:10:35 2018

@author: SCM80
"""

# =============================================================================
# 傳送資料到Twitter
# =============================================================================

import urllib.request
#import time

def send_to_twitter():
    msg="test! 看的見這段訊息嗎"
    password_manager=urllib.request.HTTPPasswordMgr()
    password_manager.add_password("Twitter API",
                                  "http://twitter.com/statuses",
                                  "@HsuJumi","CWU89GJW8K0K")
    http_handler=urllib.request.HTTPBasicAuthHandler(password_manager)
    page_opener=urllib.request.build_opener(http_handler)
    urllib.request.install_opener(page_opener)
    params=urllib.parse.urlencode({"status":msg})
    resp=urllib.request.urlopen("http://twitter.com./statuses/update.json",
                                params)
    resp.read()
    

price_now=input("你想知道當前價格嗎?(Y/N)  your answer=")
if price_now=="Y": 
    send_to_twitter()
else:
    price=99.99
    while price >4.74:
        time.sleep(3)
        price=get_price()
    
    
    
    