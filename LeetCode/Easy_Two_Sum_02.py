'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

給定一個整數array，返回兩個數字的索引，使它們相加到特定目標。
您可以假設每個輸入只有一個解決方案，並且您可能不會兩次使用相同的元素。

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

Jumi:
1. 令t=任意正整數
2. 找出向量A中，任意兩實數相加=t
'''


import random
import math
import time


# ====================================================================
# (零) 事前準備
# ====================================================================
# range(i,j,每次位移值)=i、i+1、i+2、…、j-1
name="JUMI"
for i in range(len(name)):
    print(i,name[i])
print("\n")

# list/zip/tuple/enumerate/惰性求值
for i , c in zip( range(len(name)) ,name ):
    print(i,c)
print("\n")

# enumerate
L=list( enumerate(name) )
print(L)
print("\n")


import numpy as np
import matplotlib.pyplot as plt
import seaborn
seaborn.set()
# -----
pops = np.random.randint(1,21, size=(100, 2))
print("pops母體樣本點(100點) :\n", pops)
# -----
# 利用randint隨機產生值1-20之100x2二維陣列
# 註：陣列註標索引之起始值為0，要小心!!
# -----
indices = np.random.choice(100, 20, replace=False)
# -----
# np.random.choice代表隨機抽樣之意，0-99中抽出20個樣本，
# 且抽樣後不放回(replace=False，因此不重複抽樣)



A=[]

# ====================================================================
# (一) 生成長度隨機 (<N1)，元素值隨機 (<M1) 的A向量  (random math time)
#      且向量元素值「不重複」
# ====================================================================
print("========== (一) 生出一個 長度隨機<=N1，元素值隨機但必<=M1 的A向量 ==========")

t11=time.time()
# A 的長度隨機，落在 [1,N1] 內，意同 range(1,N1+1)
# A 的每個元素，落在 [1,M1] 內，意同 range(1,M1+1)
N1=4  #長度 上限
M1=20 #元素值 上限

N1=random.sample(range(1,N1+1),1) # 隨機決定向量長度N1，range有頭無尾
N1=int(N1[0])                     # 取出來的東西為字串

print("\n")
print("隨機令向量長度= N1=",N1,"，令各元素值上限= M1=",M1)
print("\n")

#不知道怎麼宣告一個空的int變數，先令他=0
k=0

while k<N1:
    #M2必定<M1
    M2=random.sample(range(0,M1+1),1) #隨機決定M2的值
    M2=int(M2[0])
    # if M2==A[k]:
    # print("第",k+1,"個元素= 向量位置k=",k,"，第k個位置的值= M2=",M2)

    A.append(M2) #一個一個放進向量A
    k += 1       #計數+1
    
print("A向量=",A)
t12=time.time()
print("(一)花費秒數= {:>9.16f}".format(t12-t11)  )
print("\n")



# ====================================================================
# (二) 取得合乎條件的 target 範圍
# ====================================================================

target_v=[]
lenA=len(A)

t1=A[0]



# ====================================================================
# 先把比target大的剔除
# ====================================================================

