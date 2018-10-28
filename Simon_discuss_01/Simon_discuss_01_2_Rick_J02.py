import random

# t1 = datetime.now()
'''
# Create input data
'''

def createInput(digits, maxExp):
    result = []
    for i in range(digits):                       # range(digit)=[0, 999]
        result.append(random.randint(0, maxExp))  # 隨機抽一個整數，範圍[a, b]，包頭包尾
    return result




def calc(x):
    inputArray = createInput(5, 3)                #這時候 inputArray=長度5，值域[0,3]

    '''
    一個dict結構來記錄結果的答案最簡表達式
    例如： 9 = { 0: 1, 3: 1 } = 2^0 + 2^3
    '''                                           # 目標是，紀錄 9 這個數字，在二進位下，
                                                  # 2 的 k 次方位置，是 有(=1) 或 沒有(=0)


    digitMap = {}                                 # {}：字典，一個有key值的，順序可變的向量
    for i in inputArray:                          # for：會將inputArray序列中的項目，依序拉出來

        # 計算 inputArray 中的各個數字的出現次數
        digitMap[i] = digitMap.get(i, 0) + 1      # i 就是你找的對象，因為一定找不到，找不到就返回0
                                                  # 並同時指派給 digitMap 作為 key 了

        j = i                                     # 同時令 j = i，
                                                  # 因為在同一個 i 之下，要去判斷是否發生二進位

        # inputArray = [3,0,1,1,1]
        # diM[0]=1 , diM[1]=3 , diM[3]=1   等同   2^3 + 3* 2^1 + 2^0

        # 如果該位數超過 1 代表可以進位，一路往上進位
        while digitMap[j] > 1:                    # (假設j=1) 數字1的出現次數 = 2^1 的係數
                                                  # 若 >1 則表示會在二進位時進位
                                                  # => 數字2 要加1，數字1 要歸0
            digitMap[j + 1] = digitMap.get(j + 1, 0) + 1
            del digitMap[j]
            j += 1                                # 因為其實要往下一位數檢查，所以 j+1

    print("i=",i,"inputArray=",inputArray)
    
    # 最後dict結構裡面有幾個key就代表答案是多少
    return len(digitMap)
    



print("len(digitMap)=",calc(1))
