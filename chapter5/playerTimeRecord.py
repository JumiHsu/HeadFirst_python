
# 定義檔案位置
bottomPathHome = r"D:\GIT_Tortoise_Jumi_NB\HeadFirst_Python"
bottomPathOffice = r"C:\Users\Jumi_Hsu\Desktop\TortoiseGit_Jumi_jfi\HeadFirst_python"

# 匯入modual
import os
import sys
import pickle
sys.path.append(
    "C:/Users\Jumi_Hsu\Desktop\TortoiseGit_Jumi_jfi\HeadFirst_python/openTxt")
import openTxt

# 打開txt，讀取資料
fileFolder = r"\chapter5"
txtName_james = "james.txt"
txtName_julie = "julie.txt"
txtName_mikey = "mikey.txt"
txtName_sarah = "sarah.txt"

a = openTxt.changechdir_opentxt(bottomPathOffice, fileFolder, txtName_james)
print(a)

# 參數：路徑、檔案filefolder、讀取對象檔名、是否開啟工作路徑檢視

# try:
#     with open("","rb") as playerTimeRecord:
#         pickle.dump(playerTimeRecord)


# 檢查資料格式，整理乾淨成list
# sort這個list，找出前三名
