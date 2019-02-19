import os

def changeChdir(workPath):
    print("當前工作路徑 =",os.getcwd())    # 確認當前的工作路徑
    # 修改當前工作目錄
    os.chdir(workPath)
    print("變更當前工作路徑後 =",os.getcwd())

pathHome = r"D:\GIT_Tortoise_Jumi_NB\HeadFirst_Python"
pathOffice = r"C:/Users\Jumi_Hsu\Desktop\TortoiseGit_Jumi_jfi\HeadFirst_python"
fileFolder = r"\ReadFile"


# ================== 設定路徑、檔名 ==================
nowPath = pathHome
changeChdir( nowPath + fileFolder )
result_f02 = open("result02.txt")
# ================== 設定路徑、檔名 ==================

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


print("\n")
# 用 sorted(obj,reverse=True) 來幫 hash 排序
# 請這樣寫
for eachScore in sorted(scoreHash.keys(),reverse=True):
    print(scoreHash[eachScore], "had a score of",eachScore)


print("\n")
# RSA的衝浪者資料
line = "101;Johnny 'wave-boy' Johns;USA;8.32;Fish;21"
rsaHash={}

(rsaHash["ID"],rsaHash["Name"],rsaHash["Country"],rsaHash["Average"],rsaHash["Boardtype"],rsaHash["Age"])=line.split(";")

# rsaHash[ID]=Name,Country,Average,Boardtype,Age
print(rsaHash)

# def find_detail():