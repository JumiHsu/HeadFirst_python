'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

給定一個整數array，返回兩個數字的索引，使它們相加到特定目標。
您可以假設每個輸入只有一個解決方案，並且您可能不會兩次使用相同的元素。

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

Tip
題目只會給 具有唯一解 的向量nums
nums元素值不重複
target必定落在 min1+2 ~ MAX1+2 之間
檢查input2的target，找出只有一個解決方案者，放入dict中
{ target1:'[0,1]' ,target2:'[1,3]' }

'''


import random
import math
import time
import json


A=[]

# ====================================================================
# (一) 隨機生成 Nums 向量，且向量元素值「不重複」(random math time)
# ====================================================================
print("========== (一) 隨機生成 Nums 向量，且向量元素值「不重複」 ==========")

NumsLenMax = 10                            # 長度 上限
NumsElementMax = 20                        # 元素值 上限
NumsLen = random.randint( 1 ,NumsLenMax )  # 向量 長度，落在 [0,Max] 內
print("隨機向量長度 =",NumsLen,"，各元素值上限 =",NumsElementMax)

NumsElementPopulation = range( 0 ,NumsElementMax+1 )    # 留意取頭不取尾
Nums = random.sample( NumsElementPopulation ,NumsLen )  # 不重複抽取
print("向量 Nums =" ,Nums ,"\n")


# ====================================================================
# (二) 取得合乎條件的 target 範圍
# ====================================================================

# 用C幾取幾去找target

def C(m,n):
    f
    


# target_v=[]
# lenA=len(A)

# t1=A[0]



# ====================================================================
# 先把比target大的剔除
# ====================================================================











# ====================================================================
# (零) 事前準備
# ====================================================================
# range(i,j,每次位移值)=i、i+1、i+2、…、j-1
'''
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
'''

'''
values = [1, 2, 3, 4, 5, 6]
for i in range(8):
    print( random.choice(values) )
    # print( np.random.choice(100, 20, replace=False) )

print("END-1")



values = [1, 2, 3, 4, 5, 6]
for i in range(8):
    print( random.sample(values, 5) )

print("END-2")
'''


'''
import numpy
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
'''
