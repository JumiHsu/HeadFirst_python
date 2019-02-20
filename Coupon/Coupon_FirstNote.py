import random

'''
產生不重複的Coupon券代碼100份，與先前不可重複，英數混和共12碼(本身的12碼可重複?)

參考資料-dict幾個語法：
https://kaochenlong.com/2011/10/13/python-dictionary/
'''

# 先製作0~9、A~Z共10+26=36個值的索引，index=0~35
''' 生成字母表，ASCII碼表，Dec碼為10進位碼 '''
alphabet = [ chr(j) for j in range(65,91) ]
number = [chr(j) for j in range(48,58)]
elementMax = len(alphabet) + len(number)
symbolDict={}
for i in range(elementMax):  # 0~35，長度=36
    if i < len(number):
        symbolDict[i] = str(i)
    else:
        symbolDict[i] = alphabet[i-len(number)]


print(symbolDict)

# 製作一個空字典存放已產生的Coupon碼
elementMax = len(symbolDict)  # 0~35，長度=36
couponLength = 1
couponQuantityRequired = 30
couponDict = {}

# couponCodeTemp = []
# digitsLocate = 0

# 生成代碼
def generate_tempCode(couponLength, elementMax, digitsLocate=0, symbolDict=symbolDict, couponCodeTemp=[]):
    while digitsLocate < couponLength:
        index = random.randint(0, elementMax-1)  # 抽0~35，注意 randint 會包前包後
        couponCodeTemp.append(symbolDict[index])
        digitsLocate += 1
    return couponCodeTemp


# 檢查是否重複，不重複才返回code
def checkRepeat(couponCodeTemp, couponDict):
    tempCode = "".join(couponCodeTemp)

    # 如果代碼重複，則重新生成代碼，直到不重複
    while tempCode in couponDict:
        print("生成代碼重複，重新生成")
        couponCodeTempNew = generate_tempCode(
            couponLength, elementMax, digitsLocate=0, symbolDict=symbolDict, couponCodeTemp=[])
        tempNewCode = "".join(couponCodeTempNew)
        tempCode=tempNewCode

    if tempCode not in couponDict:
        return tempCode
    else:
        print("生成代碼重複，重新生成")



for i in range(couponQuantityRequired):
    # 生成代碼
    # while digitsLocate < couponLength:
    #     index = random.randint(0, elementMax-1)  # 抽0~35，注意 randint 會包前包後
    #     couponCodeTemp.append(symbolDict[index])
    #     digitsLocate += 1
    couponCodeTemp = generate_tempCode(
        couponLength, elementMax, digitsLocate=0, symbolDict=symbolDict, couponCodeTemp=[])


    # 檢查是否與 couponDict 的key重複，不重複才返回code
    # 以絕對不重複的code本身當作key值
    # tempCode = "".join(couponCodeTemp)
    tempCode = checkRepeat(couponCodeTemp, couponDict)

    # if tempCode in couponDict:
    #     print("生成代碼重複，重新生成")
    #     couponCodeTemp = generate_tempCode(couponLength, elementMax, digitsLocate=0,
    #                       symbolDict=symbolDict, couponCodeTemp=[])
    #     i += -1
    # else:
    # 比對無重複才可以正式放入變數
    locals()["couponCode_" + "%s" % (i)] = tempCode
    print("couponCode_"+str(i), "=", locals()["couponCode_" + "%s" % (i)])
    couponDict[locals()["couponCode_" + "%s" % (i)]] = "couponCode_"+str(i)
    # couponDict["couponCode_"+str(i)] = locals()["couponCode_" + "%s" % (i)]

    digitsLocate = 0
    couponCodeTemp = []


# print("\ncouponDict =", couponDict)

#     locals()["couponCode_" + "%s" % (i)] ="".join(couponCodeNow)
#     print("couponCode_"+str(i),"=", locals()["couponCode_" + "%s" % (i)])


# 做12次的取後放回的隨機抽取，得到第一次的Coupon碼

# 將Coupon碼與Coupon字典比對，找不到則放入，index從0開始命
# 進行100次，index會到99
