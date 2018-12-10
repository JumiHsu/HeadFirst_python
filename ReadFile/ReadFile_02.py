import os

print("當前工作路徑=",os.getcwd())    # 確認當前的工作路徑

result_f01 = open("result01.txt")    # 將資料來源檔案，放在工作路徑下
print(result_f01,"\n")

# 如果要變更工作路徑：os.chdir('the dir which include the file a.txt')
# #修改当前工作目录
os.chdir("D:\GIT_Tortoise_Jumi_NB\HeadFirst_Python\ReadFile")

result_f02=open("result02.txt")      # 再讀一次檔案看看
print(result_f02,"\n")

print("變更當前工作路徑=",os.getcwd())



# ===============================================
# 取得資料並找出 max (資料： result_f02)
# ===============================================
print("\n======== 取得資料並尋找 max 值========")

highest_score=0
scoreArray=[]

# 需要處理 以空白字元做分隔 的資料
# 可以用result_f02.find(" ")來尋找空白字元，也可以使用split()
# 寫法：(變數名稱1, 變數名稱2)=以空白分隔的行資料.split()
for line in result_f02:

    (name,score) = line.split()      # 特別留意，對象是line而非result_f02
    scoreArray.append(float(score))  # 每讀取一個line，就將score變數放進array

    if float(score) > highest_score: # 一邊放資料一邊尋找max
        highest_score=float(score)

result_f02.close()                   # 注意一定要加 close

print("最高分=",highest_score)
print("scoreArray=\n",scoreArray)


# ============================================
# 確認scoreArray裡面是浮點數，不是字串
# ============================================
if type(scoreArray[0]) is float :
    pass
else:
    print("scoreArray的type=",type(scoreArray[0]))






# ============================================
# 找出前三高分（方法一）
# ============================================
print("\n======== 找出前三高分（方法一） ========")

# List.sort()是一個動作，不用指定給另一個變數

# scoreArray.sort()
# scoreArray.reverse()

scoreArray.sort(reverse=True) # 同時達到 sort + reverse
print("由大到小排序後，scoreArray=\n",scoreArray)

# 前三高分
print("前三高分 =",scoreArray[0:3]) # [i,j] 注意 j=位移量
print("第 1 高分 =",scoreArray[0])
print("第 2 高分 =",scoreArray[1])
print("第 3 高分 =",scoreArray[2])


# ============================================
# 找出前三高分（方法二）
# ============================================
print("\n======== 找出前三高分（方法二） ========")

scoreArray.sort()
print("由小到大排序後，scoreArray=\n",scoreArray)

# 前三高分
print("第一高分 =",scoreArray[len(scoreArray)-1])
print("第二高分 =",scoreArray[len(scoreArray)-2])
print("第三高分 =",scoreArray[len(scoreArray)-3])


print("\n")
# 學習array
my_words = ["Jumi","KaoChin"]
print(my_words)


