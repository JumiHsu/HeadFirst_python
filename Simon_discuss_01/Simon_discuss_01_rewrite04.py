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



lengthMax = 100
elementMax = 30

A, fn, length = generateList(lengthMax,elementMax)        #生成隨機向量

print("\n目標向量 A =",A,"，向量長度 =",length,"fn =",fn,"\n")





# ----- 取 LOG 處理
logList ,fn_Log ,lengthLog ,tLog = methodLog(A)
print("logList = ",logList ,"\n")

# 檢查答案是否 = fn
if fn_Log == fn :
    pass
else:
    print( "fn =" ,fn ,"，fn_Log =" ,fn_Log ,"，答案有誤，請確認\n" )



# ----- 取 二進位 處理
binList ,fn_Bin ,lengthBin ,tBin = methodBin(A)
print("binList = ",binList ,"\n")

# 檢查答案是否 = fn
if fn_Bin == fn :
    pass
else:
    print( "fn =" ,fn ,"，fn_Bin =" ,fn_Bin ,"，答案有誤，請確認\n" )



# ----- 計算二進位後，1的個數
binNumList ,fn_BinNum ,lengthBinNum ,tBinNum  = methodBinNum(A)
print("binNumList = ",binNumList ,"\n")

# 檢查答案是否 = 前兩種算法的向量長度
if (lengthBinNum == lengthLog) and (lengthBinNum == lengthBin) :
    pass
else:
    print( "lengthLog =" ,lengthLog ,"，lengthBin =" ,lengthBin
          ,"，答案有誤，請確認\n" )




# ----- 檢查程式執行時間、別忘了回答問題(b)

method_t=[tLog ,tBin ,tBinNum]

ratioLog = tLog/min( tLog ,tBin ,tBinNum )
ratioBin = tBin/min( tLog ,tBin ,tBinNum )
ratioBinNum = tBinNum/min( tLog ,tBin ,tBinNum )

ratioFinal = {}
ratioFinal["ratioLog"] = tLog/min( tLog ,tBin ,tBinNum )
ratioFinal["ratioBin"] = tBin/min( tLog ,tBin ,tBinNum )
ratioFinal["ratioBinNum"] = tBinNum/min( tLog ,tBin ,tBinNum )
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

