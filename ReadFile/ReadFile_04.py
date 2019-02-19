import os

def changeChdir(workPath):
    print("當前工作路徑 =",os.getcwd())    # 確認當前的工作路徑
    # 修改當前工作目錄
    os.chdir(workPath)
    print("變更當前工作路徑後 =",os.getcwd())

pathHome = r"D:\GIT_Tortoise_Jumi_NB\HeadFirst_Python"
pathOffice = r"C:/Users\Jumi_Hsu\Desktop\TortoiseGit_Jumi_jfi\HeadFirst_python"
fileFolder = r"\ReadFile"


# 設定路徑
nowPath = pathHome
changeChdir( nowPath + fileFolder )

result_f02 = open("result02.txt")

highest_score=0
scoreList = []
scoreHash = {}

result_f02.seek(0)
for line in result_f02:
    (name,score) = line.split()  # 留意，對象是line而非result_f02
    scoreList.append(float(score))  # split取出的是字串，需轉浮點數
    scoreHash[score] = name  # 你的key值=score，value=name

result_f02.close()                   # 注意一定要加 close

# 兩種顯示方式
print("\n")
for eachScore in scoreHash.keys():
    print(scoreHash[eachScore], "had a score of",eachScore)

print("\n")
for eachScore,eachName in scoreHash.items():
    print(eachName,"had a score of",eachScore)


# 用 sorted(obj,reverse=True) 來幫 hash 排序

# 他不要你這樣寫
scoreListTOP3 = sorted(scoreList,reverse=True)[0:3]
scoreHashSortedTOP3 = sorted(scoreHash,reverse=True)[0:3]

print("\n最高分 =",highest_score)
print("\nscoreListTOP3 =",scoreListTOP3)
print("\nscoreHashSorted =",scoreHashSortedTOP3)
print("\n")

# 請這樣寫
for eachScore in sorted(scoreHash.keys(),reverse=True):
    print(scoreHash[eachScore], "had a score of",eachScore)

print("\n")
