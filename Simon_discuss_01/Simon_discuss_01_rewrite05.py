import random
import math
import time
import json


# =============================================================================
# 計算fn (input= 任意向量)
# =============================================================================
def calculate_fn(anyList):

    length = len(anyList)
    fn ,index = 0 ,0
    while index < length:
        fn += 2**anyList[index]
        index += 1

    return fn ,length



# =============================================================================
# 生成一個隨機向量 (input= 長度上限，元素值上限)
# =============================================================================
def generateList(lengthMax ,elementMax):

    inputList=[]
    length = random.randint(1,lengthMax)                   # randint 取頭取尾

    index = 0                         # 不知道怎麼宣告一個空的int變數，先令他=0
    while index < length:
        
        element = random.randint(1,elementMax)
        inputList.append(element)
        index += 1
    
    fn ,length = calculate_fn(inputList)

    return inputList ,fn ,length



# =============================================================================
# 生成題目向量、題目fn
# =============================================================================
def generateExampleList():

    inputList = [1,0,2,0,0,2]
    fn ,length = calculate_fn(inputList)

    return inputList ,fn ,length




# =============================================================================
# (一) 對 fn 連續取log (input= inputList)
# =============================================================================
def methodLog(inputList):
        
    t11=time.time()
    print("========== (一) LOG轉換 ==========")

    fn ,length = calculate_fn(inputList)
    fna ,bCount = fn ,0
    B1 = []

    while fna != 0:                        # fna 扣到0就結束

        B1.append( int(math.log(fna,2)) )   # 對fn取log2，取完的值取整，放入B[]

        fna += -2**B1[bCount]               # fna 扣掉 2**B[0]，剩下來的成為新的fna
        bCount += 1                        # 計數+1,雖不是用 bCount 來限制迴圈次數，
                                           # 但要用他來安排向量填入的順序
    
    fn_Log ,lengthB1 = calculate_fn(B1)
    
    t12=time.time()
    print("取 log 花費秒數= {:>9.16f}".format(t12-t11) )

    return B1 ,fn_Log ,lengthB1 ,t12-t11





# =============================================================================
# (二) 用二進位轉換來處理 (input= inputList)
# =============================================================================

def methodBin(inputList):
    
    t21=time.time()
    print("========== (二) 二進位轉換 ==========")

    fn ,length = calculate_fn(inputList)
    B2=[]
    fnBin = bin(fn)[2:]                 # 轉二進位，前面一定會加上 0b

    j=0
    for power in range(len(fnBin)-1,-1,-1):  # fnBin=1101，最高位數 = len(fnBin)-1
                                             # power=[3 2 1 0]表2進位之次方list
        if int(fnBin[j]) != 0:          # 從 fnBin第0位 開始找，若不等於0(即=1)
            B2.append(power)             # 就把 次方向量power 放入 C
            j += 1                      # 找完就找下一位

        else:
            j += 1                      # 等於0，沒事，下一位
    
    fn_Bin ,lengthB2 = calculate_fn(B2)

    t22=time.time()
    print("二進位轉換 花費秒數= {:>9.16f}".format(t22-t21) )

    return B2 ,fn_Bin ,lengthB2 ,t22-t21






# =============================================================================
# (三) 直接計算 二進位中1的個數 (input= inputList)
# =============================================================================

def methodBinNum(inputList):

    t31=time.time()
    print("========== (三) 計算 二進位中 1的個數 ==========")
    B3=[]

    fn ,length = calculate_fn(inputList)

    fnBin = bin(fn)[2:]                 # 轉二進位，前面一定會加上 0b
    fn_BinNum = None
    lengthB3 = fnBin.count("1")
    t32=time.time()

    return B3 ,fn_BinNum ,lengthB3 ,t32-t31






# =============================================================================
# (四-1) 張CHI 根據給定向量A 算fn
# =============================================================================
def chi_calculate_fn(anyList):
    
    t41=time.time()
    print("========== (四) Chi ==========")
    length = len(anyList)
    fn ,index = 0 ,0
    while index < length:
        fn += 1 << anyList[index]
        index += 1

    t42=time.time()
    return fn ,length ,t42-t41



# =============================================================================
# (四-2) 張CHI 用fn 算B向量長度
# =============================================================================
def countBit(fn):
    t41=time.time()
    count = 0
    while fn > 0:
        lsb = fn & 1      # fn和1 做bitwise and 就會只剩最右邊一個bit
        if lsb == 1:      # 最右邊一個bit 是1 等式才會成立
            count +=1

        fn = fn >> 1  #原始資料向右shift 一位
    t42=time.time()

    return count ,t42-t41






# =============================================================================
# (五) Rick
# =============================================================================
# Create input data
def createInput(digits, maxExp):
    result = []
    for i in range(digits):
        result.append(random.randint(0, maxExp))
    return result


def calc( inputList ):

    t51=time.time()
    print("========== (五) Rick ==========")
    digitMap = {}
    for i in inputList:
        # 找到對應的位數，然後+1
        # 先計算 inputList 中各個數字的出現次數
        digitMap[i] = digitMap.get(i, 0) + 1
        j = i

        # # 如果該位數超過1代表可以進位，一路往上進位
        while digitMap[j] > 1:
            digitMap[j + 1] = digitMap.get(j + 1, 0) + 1
            del digitMap[j]
            j += 1
            
    t52=time.time()
    # 最後dict結構裡面有幾個key就代表答案是多少
    return len(digitMap) ,digitMap ,t52-t51


# CHECK
def check_rick(digitMap):   # 本來 digitMap 是 dict
    B=[]
    for x in range(len(digitMap) ,-1 ,-1):
        if digitMap.get(x, 0) != 0:
            B.append(x)     # 還原為一個向量
            fn_check ,length_check = calculate_fn(B)

    return B ,fn_check ,length_check









# =============================================================================
# 主程式（使用input，會使 F5偵錯 失效，先關閉）
# =============================================================================

# 沒有寫 輸入非數字時 的錯誤信息
# print("請輸入向量長度上限、元素值上限\n（輸入0則跳過，並進行題目向量之驗證）")
# lengthMax = int(input("向量長度上限："))     # 注意input進去的是字串!! 老是錯這邊
# elementMax = int(input("元素值上限："))

# if (lengthMax == 0) or (elementMax == 0):
#     A, fn, length = generateExampleList()                     #生成題目
# elif (lengthMax != 0) and (elementMax != 0):
#     A, fn, length = generateList(lengthMax,elementMax)        #生成隨機向量
#     A, fn, length = generateExampleList()                     #生成題目
# else :
#     print("意料之外的錯誤，請檢查")



lengthMax = 100000
elementMax = 10000

A, fn, length = generateList(lengthMax,elementMax)        #生成隨機向量

print("\n目標向量 A =",A,"，向量長度 =",length,"fn =",fn,"\n")





# ----- 取 LOG 處理
logList ,fn_Log ,lengthLog ,tLog = methodLog(A)
print("logList = ",logList ,"\n" ,"B向量長=" ,lengthLog ,"\n")

# 檢查答案是否 = fn
if fn_Log == fn :
    pass
else:
    print( "fn =" ,fn ,"，fn_Log =" ,fn_Log ,"，答案有誤，請確認\n" )



# ----- 取 二進位 處理
binList ,fn_Bin ,lengthBin ,tBin = methodBin(A)
print("binList = ",binList ,"\n" ,"B向量長=" ,lengthBin ,"\n")

# 檢查答案是否 = fn
if fn_Bin == fn :
    pass
else:
    print( "fn =" ,fn ,"，fn_Bin =" ,fn_Bin ,"，答案有誤，請確認\n" )



# ----- 計算二進位後，1的個數
binNumList ,fn_BinNum ,lengthBinNum ,tBinNum  = methodBinNum(A)
print( "B向量長=" ,lengthBinNum ,"\n")

# 檢查答案是否 = 前兩種算法的向量長度
if (lengthBinNum == lengthLog) and (lengthBinNum == lengthBin) :
    pass
else:
    print( "lengthLog =" ,lengthLog ,"，lengthBin =" ,lengthBin
          ,"，答案有誤，請確認\n" )



# ----- 用張CHI的算法
fn_chi ,lengthInputChi ,tChi_1 = chi_calculate_fn(A)
lengthChi ,tChi_2 = countBit(fn_chi)

print("fn_chi =" ,fn_chi ,"\n" ,"B向量長=" ,lengthChi ,"\n")





# -----Rick的算法
lengthRick ,digitMap ,tRick = calc(A)
print("B向量長 =" ,lengthRick ,"\n")


# B ,fn_check ,length_check = check_rick(digitMap)
# print("(RECHECK) B向量 =" ,B ,"fn_check =" ,fn_check ,
#       "length_check =" ,length_check)






# ----- 檢查程式執行時間、別忘了回答問題(b)

method_t=[tLog ,tBin ,tBinNum ,tChi_1+tChi_2 ,tRick]

ratioLog = tLog /min( method_t )
ratioBin = tBin /min( method_t )
ratioBinNum = tBinNum /min( method_t )
ratioChi = (tChi_1+tChi_2) /min( method_t )
ratioRick = tRick /min( method_t )

ratioFinal = {}
ratioFinal["ratioLog"] = ratioLog
ratioFinal["ratioBin"] = ratioBin
ratioFinal["ratioBinNum"] = ratioBinNum
ratioFinal["ratioChi"] = ratioChi
ratioFinal["ratioRick"] = ratioRick
ratioFinalJson = json.dumps(ratioFinal ,indent=1)

print( ratioFinalJson )

# print(ratioFinal.items())
# ratio_min =  min(ratioFinal.items() ,key=lambda x:x[1] )
# ratio_max =  max(ratioFinal.items() ,key=lambda x:x[1] )

# print( "最快的算法 =" , ratio_min[0] )
print( "最快的算法 =" , min(ratioFinal.items() ,key=lambda x:x[1] )[0] )
print( "為 最慢算法 的：" )
print( 'percent: {:.2%}'.format( min(method_t)/max(method_t) ) )
# 不知道為何這樣會報錯
# print( 'percent: {:.2%}'.format( float(ratio_min[1]) / float(ratio_max[1]) )
print("\n")

