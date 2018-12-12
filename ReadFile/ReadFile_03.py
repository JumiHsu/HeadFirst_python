import os

def changeChdir(workPath):    
    print("當前工作路徑 =",os.getcwd())    # 確認當前的工作路徑
    # 修改當前工作目錄
    os.chdir(workPath)
    print("變更當前工作路徑後 =",os.getcwd())

    return open("result02.txt")


# home
# result_f02 = changeChdir("D:\GIT_Tortoise_Jumi_NB\HeadFirst_Python\ReadFile")
# office
result_f02 = changeChdir("C:/Users\Jumi_Hsu\Desktop\TortoiseGit_Jumi_jfi\HeadFirst_python/ReadFile")


print("\n======== 先看看 result02.txt 長怎樣 ========")
for line in result_f02:
        print(line)
result_f02.close







print("\n======== 取得資料並尋找 max 值 ========")
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

