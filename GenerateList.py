# ==================================================================
# 生成指定規則列表
# ==================================================================
import random

listLength = 10
li=[]

for i in range(listLength):
    li.append( i**2 )

print(li)



# ==================================================================
# 生成隨機列表，長度隨機、元素值也隨機
# ==================================================================
elementMax = 100
listLengthMax = 10
randomList = []

listlength = random.randint(1,listLengthMax)  # randint 取頭取尾

index = 0
while index < listLengthMax:
        
    element = random.randint(1,elementMax)
    randomList.append(element)
    index += 1



# ==================================================================
# 生成不重複隨機列表
# ==================================================================
NumsLenMax = 10                            # 長度 上限
NumsElementMax = 20                        # 元素值 上限
NumsLen = random.randint( 1 ,NumsLenMax )  # 向量 長度，落在 [0,Max] 內
print("隨機向量長度 =",NumsLen,"，各元素值上限 =",NumsElementMax)

NumsElementPopulation = range( 0 ,NumsElementMax+1 )   # 留意取頭不取尾
Nums = random.sample( NumsElementPopulation ,NumsLen ) # 不重複抽取
print("向量 Nums =" ,Nums ,"\n")
