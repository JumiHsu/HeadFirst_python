import random
import math
import time



# =============================================================================
# 生成一個隨機向量 (input= 長度上限，元素值上限)
# =============================================================================
def generateList(lengthMax,elementMax):

    A=[]
    length=random.sample(range(1,lengthMax+1),1)    # 取出物=字串，range有頭無尾
    length=int(length[0])

    fn ,index = 0 ,0                     # 不知道怎麼宣告一個空的int變數，先令他=0
    while index < length:
        
        element=random.sample(range(0,elementMax+1),1)
        element=int(element[0])                     # random.sample取出物= list
        A.append(element)
        # fn += 2**A[index]
        index += 1
    
    fn ,length = calculate_fn(A)

    return A,fn,length



# =============================================================================
# 生成題目向量、題目fn
# =============================================================================
def generateExampleList():
    A = [1,0,2,0,0,2]
        
    # length = len(A)
    # fn ,index = 0 ,0

    # while index < length:
    #     fn += 2**A[index]
    #     index += 1
    
    fn ,length = calculate_fn(A)

    return A ,fn ,length



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
# (一) 對 fn 連續取log (input= fn)
# =============================================================================
def methodLog(fn):
        
    t21=time.time()
    print("========== (一) LOG轉換 ==========")
    B=[]
    fnb,bCount = 0,0
    fna = fn
    fnaList = []

    while fna != 0:                        # fna 扣到0就結束

        fnaList.append(fna)                # 為了觀察fna的變化
        B.append( int(math.log(fna,2)) )   # 對fn取log2，取完的值取整，放入B[]

        # fnb +=  2**B[bCount]               # 再順手計算 fnb,此時 bCount=0
        fna += -2**B[bCount]               # fna 扣掉 2**B[0]，剩下來的成為新的fna
        bCount += 1                        # 計數+1,雖不是用 bCount 來限制迴圈次數，
                                           # 但要用他來安排向量填入的順序
    
    # print("fna的變化 =",fnaList)
    fnb ,length = calculate_fn(B)
    
    t22=time.time()
    print("取 log 花費秒數= {:>9.16f}".format(t22-t21) )

    return B ,fnb ,length ,(t22-t21) 





# =============================================================================
# (二) 用二進位轉換來處理 (input= fn)
# =============================================================================

def methodBin(fn):
    
    t31=time.time()
    print("========== (二) 二進位轉換 ==========")
    C=[]
    fnBin = bin(fn)[2:]
    # 轉成二進位，前面一定會被加上 0b，取 fnBin[2:] 或取 b 後的數字，即可取得實際數字
    # 最高位數 = len(fnBin)-1

    j=0
    for power in range(len(fnBin)-1,-1,-1):  # fnBin=1101  power =[3 2 1 0] 表 2進位之次方list
        if int(fnBin[j]) != 0:               # 從 fnBin 的第0位開始找，若 不等於0(即=1)，

            C.append(power)                  # 就把 次方向量power 放入 C
            j += 1                           # 找完就找下一位

        else:
            j += 1                           # =0，沒事，下一位

    fnc ,length = calculate_fn(C)

    t32=time.time()
    print("二進位轉換 花費秒數= {:>9.16f}".format(t32-t31) )

    return C ,fnc ,length ,(t32-t31) 






# =============================================================================
# 主程式
# =============================================================================

# 記得補寫錯誤信息
lengthMax=int(input("向量長度上限：")) # 特別注意input進去的是字串!!! 老是錯這邊
elementMax=int(input("元素值上限："))

# A, fn, length = generateExampleList() #生成題目
A, fn, length = generateList(lengthMax,elementMax)        #生成隨機向量

print("\n目標向量 A =",A,"，向量長度 =",length,"fn =",fn,"\n")





# ----- 取 LOG 處理
logList ,fn_Log ,lengthLog ,tLog = methodLog(fn)
print("logList = ",logList)

# 檢查答案是否 = fn
if fn_Log == fn :
    print( "fn =" ,fn ,"，fn_Log =" ,fn_Log ,"，LOG算法，答案正確\n" )
else:
    print( "fn =" ,fn ,"，fn_Log =" ,fn_Log ,"，答案有誤，請確認\n" )

#  別忘了回答問題
print( "所求B向量長度 =",lengthLog )



# ----- 取 二進位 處理
binList ,fn_Bin ,lengthBin ,tBin = methodBin(fn)
print("binList = ",binList)

# 檢查答案是否 = fn
if fn_Bin == fn :
    print( "fn =" ,fn ,"，fn_Bin =" ,fn_Bin ,"，二進位算法，答案正確\n" )
else:
    print( "fn =" ,fn ,"，fn_Bin =" ,fn_Bin ,"，答案有誤，請確認\n" )

#  別忘了回答問題
print( "所求B向量長度 =",lengthBin )
print( "使用函式 =" , )





# ----- 檢查程式執行時間
if min( tLog ,tBin ) == tLog :
    print( "LOG算法 較快!!\n\n較 二進位算法 快了：" )
    print( 'percent: {:.2%}'.format( abs(tLog-tBin)/max(tLog ,tBin) ) )

elif min( tLog ,tBin ) == tBin :
    print( "二進位算法 較快!!\n\n較 LOG算法 快了：" )
    print( 'percent: {:.2%}'.format( abs(tLog-tBin)/max(tLog ,tBin) ) )

else :
    print( "答案有誤，請確認" ,"\ntLog =" ,tLog ,"\ntBin =" ,tBin )



print("\n")

















'''

# =============================================================================
# 檢查：「取log結果 與 2進位轉換」，結果是否相同
# =============================================================================
print("========== 檢查：「取log結果 與 2進位轉換」，結果是否相同 ==========")

if B == C:
    print("檢查結果 = OK!!    相同")
elif B != C:
    print("檢查結果 = Error!!    不同")
else:
    print("Check! 其他問題!")

print("\n")

    
# =============================================================================
# 比較：「取log結果(t22-t21) 與 2進位轉換(t32-t31)」，程式需時
#       （計算程式執行時間而非CPU時間）
# =============================================================================
print("========== 比較：「取log結果 與 2進位轉換」，程式需時 ==========")

if (t32-t31) - (t22-t21) > 0:
    print("取 log 較快，較2進位快了")
    h1=((t32-t31) - (t22-t21))/(t22-t21)
    print( 'percent: {:.2%}'.format(h1)  )
elif (t32-t31) - (t22-t21) < 0:
    # print("做 二進位轉換 較快，較log快了", ((t22-t21) - (t32-t31))/(t32-t31))
    print("做 二進位轉換 較快，較log快了")
    h2=((t22-t21) - (t32-t31))/(t32-t31)
    print( 'percent: {:.2%}'.format(h2)  )
else:
    print("Check! 其他問題!")

print("\n")

# rate = .1234
# print('%.2f%%' % (rate * 100))

'''

# =============================================================================


# =============================================================================
# (二) 用二進位轉換來處理
# =============================================================================
'''
print("========== (二) 用二進位轉換來處理 ==========")


t31=time.time()
# bin轉二進位、oct轉八進位、hex轉十六進位
# fn=50

C=[]
fnBin=bin(fn)
print("fn=",fn,"，其二進位=",fnBin)

# 轉成二進位，前面一定會被加上 0b，取 fnBin[2:] 或取 b 後的數字，即可取得實際數字
fnBin=fnBin[2:]
print("fnBin的向量長度=",len(fnBin)) #最高位數 = len(fnBin)-1


j=0
for i in range(len(fnBin)-1,-1,-1):
    if int(fnBin[j]) != 0:
        C.append(i)
        # print("C向量=",C,"，i=",i,"，j=",j)
        j += 1
    else:
        # print("C向量=",C,"，i=",i,"，j=",j)
        j += 1

print("\n")
print("最終C向量=",C)

t32=time.time()
print("(三) 二進位轉換 花費秒數= {:>9.16f}".format(t32-t31) )
print("\n")

'''




'''
import time

start = time.monotonic()
time.sleep(0.1)
end = time.monotonic()
print('start : {:>9.2f}'.format(start))
print('end   : {:>9.2f}'.format(end))
print('span  : {:>9.2f}'.format(end - start))

$ python3 time_monotonic.py
start : 716028.72
end   : 716028.82
span  :      0.10
'''


'''
# 留意!! 這樣只會print出8~1，0是不會print的
for i in range(8,0,-1):
    print(i)
'''


# =============================================================================
# 測試 B[0] 是不是都等於 fn取平方根 的整數
# =============================================================================
'''
print("========== 測試 B[0] 是不是都等於 fn取平方根 的整數 ==========")

fn1=abs(math.sqrt(fn))

if B[0] == int( fn1 ) :
    print("B[0] 等於 fn取平方根 的整數")
else:
    print("不等於哦~")

'''