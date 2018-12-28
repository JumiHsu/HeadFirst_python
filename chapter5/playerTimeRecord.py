

# 定義檔案位置
bottomPathHome = r"D:\GIT_Tortoise_Jumi_NB\HeadFirst_Python"
bottomPathOffice = r"C:\Users\Jumi_Hsu\Desktop\TortoiseGit_Jumi_jfi\HeadFirst_python"

# 檔案路徑設定
nowPath = bottomPathOffice

# 匯入modual
import os
import sys
import pickle

sys.path.append(nowPath + "/nestPrint")
sys.path.append(nowPath + "/nestPrint_home")
sys.path.append(nowPath + "/openTxt")
import nestPrint
import nestPrint_home
import openTxt

# 打開txt，讀取資料，並賦值給變數
fileFolder = r"\chapter5"
txtName_james = "james.txt"
txtName_julie = "julie.txt"
txtName_mikey = "mikey.txt"
txtName_sarah = "sarah.txt"

# To Do:以locals()裏面的變數為key，做成一個字典
# Why:想要依次讀取5個檔案

#1 ==================== 寫法一 ====================
# To do:如何正確關閉檔案，jamesData.close無作用
jamesData = openTxt.changechdir_opentxt(nowPath, fileFolder, txtName_james)


# 看一下這份資料，列數過多則不列印
# To do:計數共K列，每一列印出來，在總列數<多少時全列印
jamesDataRows = len(jamesData.readlines())
print("jamesData的列數 =", jamesDataRows)

jamesData.seek(0)
for eachline in jamesData:
    print(eachline)


# 檢查資料格式，整理乾淨，放進list
jamesData.seek(0)
for eachline in jamesData:
    jamesTimeRecord = eachline.strip().split(",")
print("\njamesTimeRecord=", jamesTimeRecord)





#2 ==================== 寫法二 ====================
# 資料與程式碼在同一個路徑，所以不用引用 openTxt
jamesDataCleanB = []
with open(txtName_james) as jamesfile:
    jamesData = jamesfile.readline()
    jamesDataCleanB = jamesData.strip().split(",")
print("\njamesDataCleanB =", jamesDataCleanB)




'''
#3 錯誤寫法
# 他只有一列，split完之後已經是list了
jamesDataClean = []
jamesData.seek(0)
for eachline in jamesData:
    jamesTimeRecord = eachline.strip().split(",")
    jamesDataClean.append(jamesTimeRecord)
print("\njamesDataClean=", jamesDataClean)
'''




# print("count(-)=", eachline.count("-"))
# print("count(:)=", eachline.count(":"))
# eachline.replace("-", ".")
# eachline.replace(":", ".")

# sort這個list，找出前三名


# 把整理好的list，輸出成txt
# 參數：路徑、檔案filefolder、讀取對象檔名、是否開啟工作路徑檢視
# try:
#     with open("","rb") as playerTimeRecord:
#         pickle.dump(playerTimeRecord)
