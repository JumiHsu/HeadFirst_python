# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 19:57:22 2018

@author: SCM80
"""

# =============================================================================
# 匯入程式庫
# =============================================================================
import urllib.request
#import urllib.parse
#import urllib.error #url異常處理
#import urllib
#import urllib2
import time

# =============================================================================
# 取得目標網頁的價格資訊
# 需要import time
# =============================================================================
def make_price():
    
    #非VIP網站="http://beans-r-us.appspot.com/prices.html"
    page=urllib.request.urlopen("http://beans-r-us.appspot.com/prices-loyalty.html")
    text=page.read().decode("utf8")    

    price2_01=text.find("$")
    price2_02=text.find("</strong>")
    
    price_str=text[price2_01+1:price2_02]
    price_now=float(price_str)
    
    #兩種寫法都可以
    return(price_now)
#    return price_now

#print("嘗試印出當前價格",make_price())    


# =============================================================================
# 傳送資料到Twitter
# 目前的twitter登入頁=https://twitter.com/login?lang=zh-tw
# https://api.twitter.com/oauth/request_token
# https://twitter.com/login
# http://twitter.com/statuses
# =============================================================================
def send_to_twitter():
    msg="test"
    password_manager=urllib.request.HTTPPasswordMgr()
    password_manager.add_password("Twitter API",
                                  "https://twitter.com/login",
                                  "@HsuJumi","CWU89GJW8K0K")
    http_handler=urllib.request.HTTPBasicAuthHandler(password_manager)
    page_opener=urllib.request.build_opener(http_handler)
    urllib.request.install_opener(page_opener)
    params=urllib.parse.urlencode({'status':msg})
    params=params.encode('utf-8') #encode with utf8
    #取得HTML碼
    resp=urllib.request.urlopen("http://twitter.com/statuses/update.json",
                                params)
#    resp.read()
    resp.read().decode('utf-8')


# =============================================================================
# 程式本人
# 無存貨則立即取得價格並下訂，若存貨不足則持續關注價格，低於boss價格才下訂
# 改為：無存貨時，將價格資訊PO到twitter 試試看XD
# =============================================================================

boss=4.74
price=10.0
sleep_min=0.05


#ans=input("咖啡豆還有存貨嗎? (Y/N) 請填入=")
ans="N"
print("ans=",ans)
time.sleep(2)

if ans=="N":
    print("立刻取得當前咖啡豆價格，並且下訂")
    #取用函數，並且把return值丟到price
#    price=make_price()
#    print("當前價格=",make_price(),"請下訂")
    send_to_twitter()
    
else:

    while price>boss:
        
        #把延遲間隔拿到 make_price()的 def 外
        time.sleep(sleep_min*60)        
        
        #取用函數，並且把return值丟到price
        price=make_price()
        
        
        
        if price <= boss:
            
#            print("Hello, Boss! \n咖啡豆價格=",price,"已經比門檻價格"+str(boss)+"要低了.","請下訂單")
            send_to_twitter()
            
        else:
            print("當前價格=",price,"價格太高. plz recheck.")
        #這時候price被填入一個新的數字(當前價格)，
        #再用這個去跟boss=4.74做比較，來決定while是否運行