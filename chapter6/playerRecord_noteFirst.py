'''心得
1.把例外格式的資料用pop取出
2.使用 dict 管理不同格式的資料
3.如果不想動到原始資料，使用 copy.deepcopy
'''

# 上層路徑設定
bottomPathHome = r"D:\GIT_Tortoise_Jumi_NB\HeadFirst_Python"
bottomPathOffice = r"C:\Users\Jumi_Hsu\Desktop\TortoiseGit_Jumi_jfi\HeadFirst_python"

# 檔案夾位置設定
nowPath = bottomPathHome
fileFolder = r"\chapter6"

# 匯入modual
import os
import sys
import copy
import pickle  # 需要讀檔+輸出檔案時可以用
sys.path.append(nowPath + "/openTxt")
import openTxt

# 變更工作路徑
openTxt.changechdir(nowPath, fileFolder)


print("----------- 定義 預計會常用到的的關鍵字 ----------")
nameFourPlayers = ["james2", "julie2", "mikey2", "sarah2"]
print("nameFourPlayers =", nameFourPlayers)


print("\n----------- 讀取 原始資料 ----------")
# oriReadData = []
for each in nameFourPlayers:
    try:
        with open(each+".txt") as eachfile:
            eachdata = eachfile.readline()
            locals()["%s"%(each) + "OriData"] = eachdata.strip().split(",")
            print("\n",each+"OriData =", locals()["%s" % (each) + "OriData"], "\n")

            # oriReadData.append(locals()["%s" % (each) + "OriData"])
    except IOError as IOerr:
        print("IOError：\n",IOerr, "\n")
    except BaseException as BEerr:
        print("BaseException：\n", BEerr, "\n")



#function ------------- 整理資料：把分、秒"分開"來 ------------------------
def sanitizeString(timeString):
    if "-" in timeString:
        splitter = "-"
    elif ":" in timeString:
        splitter = ":"
    elif "," in timeString:
        splitter = ","
    else:
        return(timeString)
    (min,sec) = timeString.split(splitter)
    return (min + "." + sec)


#function ------------ 整理資料、再取集合(排除重複)，最後取排序 ---------------
def getUnigue(coachList):
    unigueSet = sorted(set([sanitizeString(each) for each in coachList]))
    return unigueSet




# ===================================================================
# list.pop(index)，你可以直接對list做pop，也可以讓她返回一個值到新變數"
# ===================================================================
james2_time = copy.deepcopy(james2OriData)
james2_name = james2_time.pop(0)
james2_birth = james2_time.pop(0)

print("\njames2OriData =",james2OriData)
print("james2_time =",james2_time)
print("james2_name =",james2_name)
print("james2_birth =",james2_birth)

#3 整理資料、再取集合(排除重複)，最後取排序
jamesTOP3 = getUnigue(james2_time)[0:3]
print("jamesTOP3 =",jamesTOP3)





print("\n----------- 【變數自動命名】自動做 4 個 ----------")
i=0
for each in nameFourPlayers:
    try:
        # 注意這邊是 deepcopy
        locals()["%s"%(each)+"_time"] = copy.deepcopy(locals()["%s"%(each)+"OriData"])

        locals()["%s"%(each)+"_name"] = locals()["%s"%(each)+"_time"].pop(0)
        locals()["%s"%(each)+"_birth"] = locals()["%s"%(each)+"_time"].pop(0)

        locals()["%s"%(each)+"TOP"] = getUnigue(locals()["%s"%(each)+"_time"])[0:3]
        print(each+"TOP =", locals()["%s" % (each)+"TOP"])
        i += 1
    except BaseException as BEerr:
        print("BaseException：",BEerr)





# ===================================================================
# 學習 dict
# ===================================================================
# # 創建
# jkDict={}
# gameDict=dict()
# print("type(jkDict) =",type(jkDict))
# print("type(gameDict) =",type(gameDict))
# # 添加 (添加的順序 != python維護的順序)
# jkDict["J"] = "Jumi"
# jkDict["K"] = "KaoChin"
# jkDict["Colors"] = ["Red","Yellow","Green","Black","White","Blue"]
# gameDict = {"Name":"pad","Android_Rank":[30,2,8,26,12,9]}
# # 查找/訪問
# print(jkDict["J"]) # Jumi
# print(gameDict["Android_Rank"][0:3]) # [30, 2, 8]
# print(sorted(gameDict["Android_Rank"])[0:3]) # [2, 8, 9]


# ===================================================================
print("\n-------- 【改用dict】改寫代碼 (先一次一個) -------")
# ===================================================================
james2_time = copy.deepcopy(james2OriData)  # 注意要用深拷貝

james2_dict = {}
james2_dict["name"] = james2_time.pop(0)
james2_dict["birth"] = james2_time.pop(0)
james2_dict["time"] = james2_time

print("\njames2_dict =",james2_dict)
print("\njames2OriData =",james2OriData)

print("\njames2_dict[time] =",james2_dict["time"])
print("james2_dict[name] =",james2_dict["name"])
print("james2_dict[birth] =",james2_dict["birth"])


#3 getUnigue：整理資料、取集合(排除重複)，return 後取排序
jamesTOP3 = getUnigue(james2_dict["time"])[0:3]
print(james2_dict["name"],"TOP3 =",jamesTOP3)

