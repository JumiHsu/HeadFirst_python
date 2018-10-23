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

A=[]

# ====================================================================
# (一) 生成長度隨機 (<N1)，元素值隨機 (<M1) 的A向量  (random math time)
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
    # print("第",k+1,"個元素= 向量位置k=",k,"，第k個位置的值= M2=",M2)

    A.append(M2) #一個一個放進向量A
    k += 1       #計數+1
    
print("A向量=",A)
t12=time.time()
print("(一)花費秒數= {:>9.16f}".format(t12-t11)  )
print("\n")



# ====================================================================
# (二) 判斷輸入的 target 必須為正整數
# ====================================================================
target = input("請輸入一個正整數：")
target = int(target)                # 切記要轉int

while target <= 0:
    
    if target == 0 :
        target = input("正整數不包含 0 哦，請重新輸入一個正整數：")
    elif target < 0 :
        target = input("正整數是指 大於0 的整數。請重新輸入一個正整數：")


    # else後面不用寫條件，因為else一定要是補集合

    else  :
        # print("您輸入的正整數為：",target) # 這樣寫會錯，就算輸入正整數也不會出現這句
        # 如果else後面什麼都不寫，也會錯，他會以為target那一句是縮排縮錯了XD?
        # 或者我應該用 pass

        break                       # break 則可以
                
    target = int(target)    # user會多次重新輸入，所以迴圈內，每次輸入完後要重新轉int

print("最終確認，您輸入的正整數為：",target)



# ====================================================================
# 先把比target大的剔除
# ====================================================================

