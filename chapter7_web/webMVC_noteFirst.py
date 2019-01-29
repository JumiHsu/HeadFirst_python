
# 上層路徑設定
bottomPathHome = r"D:\GIT_Tortoise_Jumi_NB\HeadFirst_Python"
bottomPathOffice = r"C:\Users\Jumi_Hsu\Desktop\TortoiseGit_Jumi_jfi\HeadFirst_python"

# 檔案夾位置設定
btmPath = bottomPathOffice
fileFolder = r"\chapter7_web"

# 匯入modual
import os
import sys
import pickle  # 需要讀檔+輸出檔案
sys.path.append(btmPath + "/openTxt")
sys.path.append(btmPath + "/athleteList")
import openTxt
import athleteList

# 變更工作路徑
openTxt.changechdir(btmPath, fileFolder)



print("----------- 定義 預計會常用到的的關鍵字 ----------")
nameFourPlayers = ["james", "julie", "mikey", "sarah"]
# nameFourPlayers[0]+".txt"
print("nameFourPlayers =", nameFourPlayers, "\n")







# 使用 import 的 module：athleteList
# 一次只要處理一個 name 就好


'''
丟進4個名字
讀取那4個名字的txt
用pickle存起來
存成一個長度=4的，以名字為key的字典
# '''
# def put_to_store(nameList):
#     for eachName in nameList:
#         # with open(eachName+".txt") as locals()["%s" % (eachName) + "Data"]:
#         with open(eachName+".txt") as eachName+"Data":
#             pickle.dump(eachName+"Data", eachName+"Data")
#     return a


'''
讀取檔案 (用pickle)
輸出的時候輸出成 一個長度=4，以名字為key，其值為athleteList class物件的字典
'''
# def get_from_store(b):
#     return b


# ========================================================================
# 【製作】創建符合 AthleteList類型 的 instance
# ========================================================================
for each in nameFourPlayers:
    rank = 3
    locals()["%s" % (each) +
             "OriData"] = athleteList.get_coach_data(each+".txt")
    print(each+"OriData =", locals()["%s" % (each) + "OriData"])

    # locals()["%s" % (each) +
    #          "OriTime"] = athleteList.get_coach_data(each+".txt").time
    # print(each+"OriTime =", locals()["%s" % (each) + "OriTime"])

    locals()["%s" % (each) + "TOP3"] = locals()["%s" %
                                                (each) + "OriData"].TOP(rank)
    print(locals()["%s" % (each) + "OriData"].name, "TOP3 =",  # 改成直接用 obj.name去呼叫
          locals()["%s" % (each) + "TOP3"], "\n")


