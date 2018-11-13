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
    length = random.randint(1,lengthMax)           # randint 取頭取尾

    index = 0                 # 不知道怎麼宣告一個空的int變數，先令他=0
    while index < length:
        
        element = random.randint(1,elementMax)
        inputList.append(element)
        index += 1
    # inputList = []    # 假設要給定指定向量

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

    fn ,length = calculate_fn(inputList)
    fna ,bCount = fn ,0
    B1 = []

    while fna != 0:                        # fna 扣到0就結束

        B1.append( int(math.log(fna,2)) )   # 對fn取log2，取完的值取整，放入B[]

        fna += -(2**B1[bCount])            # fna 扣掉 2**B[0]，剩下來的成為新的fna
        bCount += 1                        # 計數+1,雖不是用 bCount 來限制迴圈次數，
                                           # 但要用他來安排向量填入的順序
    
    fn_Log ,lengthB1 = calculate_fn(B1)

    return B1 ,fn_Log ,lengthB1





# =============================================================================
# (二)-1 用二進位轉換來處理 (input= inputList)
# =============================================================================

def methodBin(inputList):
    
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

    return B2 ,fn_Bin ,lengthB2






# =============================================================================
# (二)-2 直接計算 二進位中1的個數 (input= inputList)
# =============================================================================

def methodBinNum(inputList):

    B3=[]

    fn ,length = calculate_fn(inputList)

    fnBin = bin(fn)[2:]                 # 轉二進位，前面一定會加上 0b
    fn_BinNum = None
    lengthB3 = fnBin.count("1")

    return B3 ,fn_BinNum ,lengthB3






# =============================================================================
# (三) KAO (input= inputList)
# =============================================================================
def SolutionA(inputList):
    
    tempN = 0
    for i in range(len(inputList)):
        tempN += pow(2,inputList[i])
    #print(tempN)
    return tempN

def FindNearestBinarySolution(B): # B起初=fn
    num = 0
    while pow(2,num) <= B:
        num += 1
    return num-1

def GetBinarySquareSolution(ARR):
    finalnum = 0
    for i in range(len(ARR)):
        finalnum += pow(2,ARR[i])
    #print(finalnum)
    return finalnum






# =============================================================================
# (四-1) 張CHI 根據給定向量A 算fn
# =============================================================================
def chi_calculate_fn(anyList):
    
    length = len(anyList)
    fn ,index = 0 ,0
    while index < length:
        fn += 1 << anyList[index]
        index += 1

    return fn ,length



# =============================================================================
# (四-21) 張CHI 用fn 算B向量長度，方法1
# =============================================================================
def countBit(fn):
    
    count = 0
    while fn > 0:
        lsb = fn & 1      # fn和1 做bitwise and 就會只剩最右邊一個bit
        if lsb == 1:      # 最右邊一個bit 是1 等式才會成立
            count +=1

        fn = fn >> 1  #原始資料向右shift 一位

    return count



# =============================================================================
# (四-22) 張CHI 用fn 算B向量長度，方法2
# =============================================================================
def superCount(fn):
    v = fn
    v = ( v & 0x55555555 ) + ((v>> 1) & 0x55555555) # v1
    v = ( v & 0x33333333 ) + ((v>> 2) & 0x33333333) # v2
    v = ( v & 0x0f0f0f0f ) + ((v>> 4) & 0x0f0f0f0f) # v3
    v = ( v & 0x00ff00ff ) + ((v>> 8) & 0x00ff00ff) # v4
    v = ( v & 0x0000ffff ) + ((v>>16) & 0x0000ffff) # v5
    return v






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
            

    # 最後dict結構裡面有幾個key就代表答案是多少
    return len(digitMap) ,digitMap


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



lengthMax = 10000
elementMax = 1000

A, fn, length = generateList(lengthMax,elementMax)        #生成隨機向量

print("\n目標向量 A =",A,"，向量長度 =",length,"fn =",fn,"\n")





# ----- (一)取 LOG 處理
print("========== (一) LOG轉換 ==========")
t1=time.time()

logList ,fn_Log ,lengthLog , = methodLog(A)

t2=time.time()
tLog = t2 - t1
print("tLog = {:>9.16f}".format(tLog) )
print("B向量長=" ,lengthLog ,"\n")

# 檢查答案是否 = fn
if fn_Log == fn :
    pass
else:
    print( "fn =" ,fn ,"，fn_Log =" ,fn_Log ,"，答案有誤，請確認\n" )



# ----- (二)-1 取 二進位 處理
print("========== (二)-1 二進位轉換 ==========")
t1=time.time()

binList ,fn_Bin ,lengthBin = methodBin(A)

t2=time.time()
tBin = t2 - t1
print("tBin = {:>9.16f}".format(tBin) )
print("B向量長=" ,lengthBin ,"\n")

# 檢查答案是否 = fn
if fn_Bin == fn :
    pass
else:
    print( "fn =" ,fn ,"，fn_Bin =" ,fn_Bin ,"，答案有誤，請確認\n" )



# ----- (二)-2 計算二進位後，1的個數
print("========== (二)-2 計算二進位後，1的個數 ==========")
t1=time.time()

binNumList ,fn_BinNum ,lengthBinNum = methodBinNum(A)

t2=time.time()
tBinNum = t2 - t1
print("tBinNum = {:>9.16f}".format(tBinNum) )
print( "B向量長=" ,lengthBinNum ,"\n")



# 檢查答案是否 = 前兩種算法的向量長度
if (lengthBinNum == lengthLog) and (lengthBinNum == lengthBin) :
    pass
else:
    print( "lengthLog =" ,lengthLog ,"，lengthBin =" ,lengthBin
          ,"，答案有誤，請確認\n" )



# ----- (三)高謙的算法
print("========== (三) KAO ==========")
t1=time.time()

nSol = SolutionA(A)
nTempSol = nSol
# print("nSol =" ,nSol)
nNearest = FindNearestBinarySolution(nSol)
arrSol = [nNearest]
# print("arrSol=",arrSol)

while nSol != GetBinarySquareSolution(arrSol):
    nTempSol -= pow(2,nNearest)
    nNearest = FindNearestBinarySolution(nTempSol)
    arrSol.append(nNearest)

t2=time.time()
tKAO = t2 - t1
print("tKAO = {:>9.16f}".format(tKAO) )
print("B向量長=" ,len(arrSol) ,"\n")


# 檢查答案是否 = fn
if nSol == fn:
    pass
else:
    print("fn =" ,fn ,"，nSol =" ,nSol ,"，答案有誤，請確認\n")




# ----- (四)-21 張CHI的算法1

print("========== (四)-1 Chi ==========")
t1=time.time()

fn_chi_1 ,lengthInputChi = chi_calculate_fn(A)
lengthChi_1 = countBit(fn_chi_1)

t2=time.time()
tChi_1 = t2 - t1
print("tChi_1 = {:>9.16f}".format(tChi_1) )
print("B向量長=" ,lengthChi_1 ,"\n")
print("fn_chi_1 =" ,fn_chi_1 ,"\n")


# ----- (四)-22 用張CHI的算法2
print("========== (四)-2 Chi ==========")
t1=time.time()

fn_chi_2 ,lengthInputChi = chi_calculate_fn(A)
lengthChi_2 = superCount(fn_chi_2)

t2=time.time()
tChi_2 = t2 - t1
print("tChi_1 = {:>9.16f}".format(tChi_2) )
print("B向量長=" ,lengthChi_2 ,"\n")
print("fn_chi_2 =" ,fn_chi_2 ,"\n")


# ----- (五) Rick的算法
print("========== (五) Rick ==========")
t1=time.time()

lengthRick ,digitMap = calc(A)

t2=time.time()

tRick = t2 - t1
print("tChi_1 = {:>9.16f}".format(tRick) )
print("B向量長 =" ,lengthRick ,"\n")


# B ,fn_check ,length_check = check_rick(digitMap)
# print("(RECHECK) B向量 =" ,B ,"fn_check =" ,fn_check ,
#       "length_check =" ,length_check)






# ----- 檢查程式執行時間

# 將新增的 算法耗時t 放進來
method_t=[tLog ,tBin ,tBinNum ,tKAO ,tChi_1 ,tChi_2 ,tRick]

ratioLog = tLog /min( method_t )
ratioBin = tBin /min( method_t )
ratioBinNum = tBinNum /min( method_t )
ratioKAO = tKAO /min( method_t )
ratioChi_1 = tChi_1 /min( method_t )
ratioChi_2 = tChi_2 /min( method_t )
ratioRick = tRick /min( method_t )

ratioFinal = {}
ratioFinal["ratioLog"] = ratioLog
ratioFinal["ratioBin"] = ratioBin
ratioFinal["ratioBinNum"] = ratioBinNum
ratioFinal["ratioKAO"] = ratioKAO
ratioFinal["ratioChi_1"] = ratioChi_1
ratioFinal["ratioChi_2"] = ratioChi_2
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

