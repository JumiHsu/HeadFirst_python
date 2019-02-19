import random

'''
產生不重複的Coupon券代碼100份，與先前不可重複，英數混和共12碼(本身的12碼可重複?)
'''

# 先製作0~9、A~Z共10+26=36個值的索引，index=0~35
''' 生成字母表，ASCII碼表，Dec碼為10進位碼 '''
alphabet = [ chr(j) for j in range(65,91) ]
number = [chr(j) for j in range(48,58)]
symbolDict={}
for i in range(36):  # 0~35，長度=36
    if i < len(number):
        symbolDict[i] = str(i)
    else:
        symbolDict[i] = alphabet[i-len(number)]


# 製作一個空字典存放已產生的Coupon碼
elementMax = len(symbolDict)  # 0~35，長度=36
couponLength = 3
couponQuantityRequired = 5
couponDict = {}

couponCodeTemp = []
digitsLocate = 0
for i in range(couponQuantityRequired):
    while digitsLocate < couponLength:
        index = random.randint(0, elementMax-1)  # 抽0~35，注意 randint 會包前包後
        couponCodeTemp.append(symbolDict[index])
        digitsLocate += 1

    # 這邊我需要比對 couponDict ，是否與現有的code重複
    # 以絕對不重複的code本身當作key值

    # 比對無重複才可以正式放入變數
    locals()["couponCode_" + "%s" % (i)] = "".join(couponCodeTemp)
    print("couponCode_"+str(i), "=", locals()["couponCode_" + "%s" % (i)])
    couponDict["couponCode_"+str(i)] = locals()["couponCode_" + "%s" % (i)]

    digitsLocate = 0
    couponCodeTemp = []


print("\ncouponDict =", couponDict)

#     locals()["couponCode_" + "%s" % (i)] ="".join(couponCodeNow)
#     print("couponCode_"+str(i),"=", locals()["couponCode_" + "%s" % (i)])


# 做12次的取後放回的隨機抽取，得到第一次的Coupon碼

# 將Coupon碼與Coupon字典比對，找不到則放入，index從0開始命
# 進行100次，index會到99
