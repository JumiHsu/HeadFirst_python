import random
import math
import time



# =============================================================================
# 生成一個隨機向量 (input= 長度上限，元素值上限)
# =============================================================================
def generateList(lengthMax ,elementMax):

    inputList=[]
    length = random.randint(1,lengthMax)        # randint 取頭取尾

    fn ,index = 0 ,0                  # 不知道怎麼宣告一個空的int變數，先令他=0
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
# (一) 對 fn 連續取log (input= inputList)
# =============================================================================
def methodLog(inputList):
        
    t21=time.time()
    print("========== (一) LOG轉換 ==========")

    fn ,length = calculate_fn(inputList)
    fna ,bCount = fn ,0
    B = []
    # fnaList = []

    while fna != 0:                        # fna 扣到0就結束

        # fnaList.append(fna)                # 為了觀察fna的變化
        B.append( int(math.log(fna,2)) )   # 對fn取log2，取完的值取整，放入B[]

        # fnb +=  2**B[bCount]             # 再順手計算 fnb,此時 bCount=0
        fna += -2**B[bCount]               # fna 扣掉 2**B[0]，剩下來的成為新的fna
        bCount += 1                        # 計數+1,雖不是用 bCount 來限制迴圈次數，
                                           # 但要用他來安排向量填入的順序
    
    # print("fna的變化 =",fnaList)
    fn_Log ,length = calculate_fn(B)
    
    t22=time.time()
    print("取 log 花費秒數= {:>9.16f}".format(t22-t21) )

    return B ,fn_Log ,length ,(t22-t21) 





# =============================================================================
# (二) 用二進位轉換來處理 (input= inputList)
# =============================================================================

def methodBin(inputList):
    
    t31=time.time()
    print("========== (二) 二進位轉換 ==========")

    fn ,length = calculate_fn(inputList)
    C=[]
    fnBin = bin(fn)[2:]
    # 轉二進位，前面一定會加上 0b，取 fnBin[2:]，即可取得實際數字
    # 最高位數 = len(fnBin)-1

    j=0
    for power in range(len(fnBin)-1,-1,-1):  # fnBin=1101
                                             # power=[3 2 1 0]表2進位之次方list
        if int(fnBin[j]) != 0:          # 從 fnBin第0位 開始找，若不等於0(即=1)
            C.append(power)             # 就把 次方向量power 放入 C
            j += 1                      # 找完就找下一位

        else:
            j += 1                      # 等於0，沒事，下一位
    
    fn_Bin ,length = calculate_fn(C)

    t32=time.time()
    print("二進位轉換 花費秒數= {:>9.16f}".format(t32-t31) )

    return C ,fn_Bin ,length ,(t32-t31) 






# =============================================================================
# 主程式（生成隨機向量會壞掉）
# =============================================================================

# 記得補寫錯誤信息
print("請輸入向量長度上限、元素值上限\n（輸入0則跳過，並進行題目向量之驗證）")
lengthMax = int(input("向量長度上限："))     # 注意input進去的是字串!! 老是錯這邊
elementMax = int(input("元素值上限："))

if (lengthMax == 0) or (elementMax == 0):
    A, fn, length = generateExampleList()                     #生成題目
elif (lengthMax != 0) and (elementMax != 0):
    # A, fn, length = generateList(lengthMax,elementMax)        #生成隨機向量
    A, fn, length = generateExampleList()                     #生成題目
else :
    print("意料之外的錯誤，請檢查")





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



# ----- 檢查程式執行時間、別忘了回答問題
if min( tLog ,tBin ) == tLog :
    print( "LOG算法 較快!!\n\n較 二進位算法 快了：" )
    print( 'percent: {:.2%}'.format( abs(tLog-tBin)/max(tLog ,tBin) ) )

    print( "所求 B 向量長度 =",lengthLog ,"\n")
    print( "使用函式 = methodLog(A)" )

elif min( tLog ,tBin ) == tBin :
    print( "二進位算法 較快!!\n\n較 LOG算法 快了：" )
    print( 'percent: {:.2%}'.format( abs(tLog-tBin)/max(tLog ,tBin) ) )

    print( "所求B向量長度 =",lengthBin ,"\n")
    print( "使用函式 = methodBin(A)" )

else :
    print( "答案有誤，請確認" ,"\ntLog =" ,tLog ,"\ntBin =" ,tBin )



print("\n")
