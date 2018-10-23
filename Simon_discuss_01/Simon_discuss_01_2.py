import random
import math
import time
# time：http://www.runoob.com/python/python-date-time.html
# time：https://pythoncaff.com/docs/pymotw/time-time-module/97

A=[]
B=[]

# # ====================================================================
# # (一) 想辦法生出一個長度隨機<N1，元素值隨機但必<N2 的A向量
# # ====================================================================
print("========== (一) 生出一個 長度隨機<=N1，元素值隨機但必<=K1 的A向量 ==========")

t11=time.time()

# A 的長度隨機，落在 [1,100000] 內，令 N1=100000
# A 的每個元素，落在 [0,10000]  內，令 K1=10000
N1=50 #100000
K1=8 #10000

N1=random.sample(range(1,N1+1),1) # 隨機決定向量長度N1，取出來的東西為字串，range有頭無尾
N1=int(N1[0])

print("\n")
print("隨機取得向量長度= N1=",N1,"，令各元素值上限= K1=",K1)
print("\n")

#不知道怎麼宣告一個空的int變數，先令他=0
fn=0
k=0

while k<N1:
    #K2必定<K1
    K2=random.sample(range(0,K1+1),1) #隨機決定K2的值
    K2=int(K2[0])    
    # print("第",k+1,"個元素= 向量位置k=",k,"，第k個位置的值= K2=",K2)

    A.append(K2)
    
    fn += 2**A[k]
    k += 1
    
print("A向量=",A)
print("binarian of A= fn=",fn)

t12=time.time()
print("(一)花費秒數= {:>9.16f}".format(t12-t11)  )
print("\n")

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




# ====================================================================
# (一) 令一個固定的A向量、fn，作為測試對象
# ====================================================================
# print("========== (一) 令一個固定的A向量、fn，作為測試對象 ==========")

# t11=time.time()
# A = [1,0,2,0,0,2]

# # 計算出該 A向量 的fn是多少
# n = len(A)
# fn = 0
# sum=0

# while sum<n:
#     fn += 2**A[sum]
#     sum += 1

# print("A向量=",A,"，A向量長度=",n,"；對應的fn=",fn)
# print("\n")

# t12=time.time()
# print("(一)花費秒數= {:>9.16f}".format(t12-t11)  )




# ====================================================================
# (二) 用 對fn 連續取log來回推B
# ====================================================================
print("========== (二) 用連續取log來處理 ==========")

t21=time.time()

fnb=0
sumb=0
fna=fn
fna_v=[]

while fna != 0:

    #對fn取log2，取完的值取整，放入B[0]
    
    # print("fn= fna=",fna)
    fna_v.append(fna)
    B.append( int(math.log(fna,2)) ) # 先把取log2後取整的值放入B[0]
    # print("sumb=",sumb)
    # print("B[0]=",B[0])
    # print("B[sumb]=",B[sumb])
    # print("\n")

    fnb +=  2**B[sumb]               # 再順手計算 bn,此時 sumb=0
    fna += -2**B[sumb]               # fna 扣掉 2**B[0]，剩下來的成為新的fna
    sumb += 1                        # 計數+1,雖不是用sumb來限制迴圈次數，但要用他來安排向量填入的順序

print("fna的變化 =",fna_v)
print("\n")
print("最終B向量 =",B,"fnb =",fnb)


t22=time.time()
print("(二)取 log 花費秒數= {:>9.16f}".format(t22-t21) )
print("\n")


# ====================================================================
# 測試 B[0] 是不是都等於 fn取平方根 的整數
# ====================================================================
'''
print("========== 測試 B[0] 是不是都等於 fn取平方根 的整數 ==========")

fn1=abs(math.sqrt(fn))

if B[0] == int( fn1 ) :
    print("B[0] 等於 fn取平方根 的整數")
else:
    print("不等於哦~")

'''

'''
# 留意!! 這樣只會print出8~1，0是不會print的
for i in range(8,0,-1):
    print(i)
'''




# ====================================================================
# (三) 用二進位轉換來處理
# ====================================================================
print("========== (三) 用二進位轉換來處理 ==========")


t31=time.time()
# bin轉二進位、oct轉八進位、hex轉十六進位
# fn=50

C=[]
fn2=bin(fn)
print("fn=",fn,"，其二進位=",fn2)

# 轉成二進位，前面一定會被加上 0b，取 fn2[2:] 或取 b 後的數字，即可取得實際數字
fn2=fn2[2:]
print("fn2的向量長度=",len(fn2)) #最高位數 = len(fn2)-1


j=0
for i in range(len(fn2)-1,-1,-1):
    if int(fn2[j]) != 0:
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



# ====================================================================
# 檢查：「取log結果 與 2進位轉換」，結果是否相同
# ====================================================================
print("========== 檢查：「取log結果 與 2進位轉換」，結果是否相同 ==========")

if B == C:
    print("檢查結果 = OK!!    相同")
elif B != C:
    print("檢查結果 = Error!!    不同")
else:
    print("Check! 其他問題!")

print("\n")

    
# ====================================================================
# 比較：「取log結果(t22-t21) 與 2進位轉換(t32-t31)」，程式需時
#       （計算程式執行時間而非CPU時間）
# ====================================================================
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