import random

# Create input data
def createInput(digits, maxExp):
	result = []
	for i in range(digits):
		result.append(random.randint(0, maxExp))
	return result

def calc(x):
	inputArray = createInput(1000, 100)

	'''
		一個dict結構來記錄結果的答案最簡表達式
		例如： 9 = { 0: 1, 3: 1 } = 2^0 + 2^3
	'''
	digitMap = {}
	for i in inputArray:
		# 找到對應的位數，然後+1
		digitMap[i] = digitMap.get(i, 0) + 1
		j = i

		# 如果該位數超過1代表可以進位，一路往上進位
		while digitMap[j] > 1:
			digitMap[j + 1] = digitMap.get(j + 1, 0) + 1
			del digitMap[j]
			j += 1

	# 最後dict結構裡面有幾個key就代表答案是多少
	return len(digitMap)

print(calc(1))
