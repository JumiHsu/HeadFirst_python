import random
from datetime import datetime

t1 = datetime.now()

'''
# Create input data
'''
# 隨機生成一個向量result，長度=[1,]，值域=[0,100]

def createInput(digits, maxExp):
	result = []                                   # []：有序向量
	for i in range(digits):                       # range(digit)=[0, 999]
		result.append(random.randint(0, maxExp))  # 隨機抽一個整數，範圍[a, b]，包頭包尾
	return result


def calc(x):
	inputArray = createInput(5, 3)                #這時候 inputArray=長度5，值域[0,3]

	'''
		一個dict結構來記錄結果的答案最簡表達式
		例如： 9 = { 0: 1, 3: 1 } = 2^0 + 2^3
	'''                                           # 上述的意思是，紀錄9這個數字，的二進位下，
                                                  # 2 的 k 次方位置，是 有(=1) 或 沒有(=0)


	digitMap = {}                                 # {}：字典，一個有key值的，順序可變的向量
	for i in inputArray:                          # for：會將inputArray序列中的項目，依序拉出來
		
		# 找到對應的位數，然後+1
		# 計算 inputArray 中的各個數字的出現次數
		digitMap[i] = digitMap.get(i, 0) + 1      # i 就是你找的對象，因為一定找不到，找不到就返回0
		                                          # 並同時指派給 digitMap 作為 key 了
		j = i

		# 如果該位數超過1代表可以進位，一路往上進位
		while digitMap[j] > 1:
			digitMap[j + 1] = digitMap.get(j + 1, 0) + 1
			del digitMap[j]
			j += 1

	print("i=",i,"inputArray=",inputArray)
    
    # 最後dict結構裡面有幾個key就代表答案是多少
	return len(digitMap)
    
print("len(digitMap)=",calc(1))

t2 = datetime.now()
print("t1=",t1,"\nt2=",t2,"\nt2-t1=",t2-t1)



# 字典：http://www.runoob.com/python3/python3-dictionary.html
# get()：http://www.runoob.com/python3/python3-att-dictionary-get.html

# dict.get(要索引的key, default=None)，如果指定key的值不存在，則填入default。
# dict[i] 和 digitMap.get(i, 0) 的差別：
# https://blog.csdn.net/aaazz47/article/details/79022644