import random
import math
import time

# ====================================================================
# 生成一個隨機向量 定義長度上限、元素值上限
# ====================================================================

def generateList(lengthMax,elementMax):
    print("========== (一) 生成一個隨機向量 定義長度上限、元素值上限 ==========")

    t11 = time.time()
    length = random.sample(range(1,lengthMax+1),1)        # 取出物=字串，range有頭無尾
    length = int(length[0])

    fn ,index = 0 ,0                                    # 不知道怎麼宣告一個空的int變數，先令他=0

    while index < length:
        
        element=random.sample(range(0,elementMax+1),1)  # 注意random.sample取出的東西 = list
        element=int(element[0])
        # print("第",index+1,"個元素= 向量位置",index,"，其值為：",element)
        A.append(element)

        fn += 2**A[index]
        index += 1
    
    t12=time.time()
    print("(一)花費秒數= {:>9.16f}".format(t12-t11)  )
                                                        # 其實是 return 一個 tuple，可以省略括號
    return A,fn,length                                  # 且多個變數可同時接收一個 tuple，按位置指派值




# ====================================================================
# 主程式
# ====================================================================

A=[]
B=[] # LOG作法
C=[] # 二進位作法

# 記得補寫錯誤信息
# lengthMax = int(input("向量長度上限："))    # 特別注意input進去的是字串! 老是錯這邊
# elementMax = int(input("元素值上限："))

lengthMax = 5
elementMax = 4

A, fn, length = generateList(lengthMax,elementMax)

print("\n隨機向量長度=",length,"，各元素值上限=",elementMax)
print("A向量 =",A,"fn =",fn,"\n")



fn2 = bin(fn)[2:]       # 此時 fn2 是個字串
fn2List = list(fn2)
print("fn2 =" ,fn2 ,"fn2List =" ,fn2List)

fn2_Dict = {}
keyList = []


# 生成另外一個key值list，再zip keyList 和 fn2List
for i in range( len(fn2)-1 ,-1 ,-1 ):     # 逆著4,3,2,1,0的時候，別忘了是range(4,-1,-1)
    keyList.append(i)

print("keyList =",keyList)                # keyList = [3,2,1,0]
print("\n")

fn2_Dict = dict( zip( keyList , fn2 ))
print(fn2_Dict)



'''
# 創建一個新的字典
# for i in keyList:

for j in range( len(fn2)-1 ):             # j = 0 1 2 3
    # tempDict = tempDict.fromkeys( keyList, fn2List[j] )
    # tempDict = tempDict.fromkeys( i, fn2List[j] )
    # fn2_Dict[ keyList[j] ] = fn2List[j]
    

    print("j =" ,j ,"fn2List[j] =" ,fn2List[j])
    print("fn2_Dict =" ,fn2_Dict)
    print("\n")


for j in range( len(fn2)-1 ):
    fn2_Dict = keyList:fn2[j] # 把資料指派給字典
'''



# fn2_Dict = zip( keyList , fn2 )
# for each in zip( keyList , fn2 ) :
# print(each)
# print("不each的話，fn2_Dict =",fn2_Dict)


'''

for i in range( len(fn2)-1 ,-1 ,-1 ):     # 逆著4,3,2,1,0的時候，別忘了是range(4,-1,-1)
    for j in range( len(fn2)-1 ):



        # fn2_Dict[ i : fn2[j] ]



print("fn2_Dict =",fn2_Dict)


'''


