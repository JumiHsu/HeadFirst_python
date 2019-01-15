'''心得
1.讓函數一次只做一件事 (最後再以某個方式重複他)
    a.讀取完檔案，還是可以一併先扔進一個AllDataList，一讀完就丟
    b.只是後續的中間過程，依然一次只處理一件事
    c.最後再利用 a.整理好的 AllDataList，去做批次性的處理
2.工作路徑
3.List Comprehension
4.動態變數命名
5.處理重複資料：
    a.使用set，留意set後順序會變
    b.手動:設定空list，用not in
    c.手動:設定target依次比對
6.聰明的整理資料
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
import pickle  # 需要讀檔+輸出檔案時可以用
sys.path.append(nowPath + "/openTxt")
import openTxt

# 變更工作路徑
openTxt.changechdir(nowPath, fileFolder)


print("----------- 定義 預計會常用到的的關鍵字 ----------")
nameFourPlayers = ["james2", "julie2", "mikey2", "sarah2"]
print("nameFourPlayers =", nameFourPlayers)


#1 打開並讀取txt，並指派給變數，
# 額外把四筆ori資料，塞進一個list
print("\n----------- 原始資料 ----------")
# oriReadData = []
for each in nameFourPlayers:
    try:
        with open(each+".txt") as eachfile:
            eachdata = eachfile.readline()
            locals()["%s"%(each) + "OriData"] = eachdata.strip().split(",")
            print(each+"OriData =", locals()["%s" % (each) + "OriData"], "\n")

            # oriReadData.append(locals()["%s" % (each) + "OriData"])
    except IOError as IOerr:
        print("IOError：\n",IOerr, "\n")
    except BaseException as BEerr:
        print("BaseException：\n", BEerr, "\n")

print("james2OriData =",james2OriData)

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
print("\nlist.pop(index)，你可以直接對list做pop，也可以讓她返回一個值到新變數")
# ===================================================================

james2_time = james2OriData
james2_name = james2_time.pop(0)
james2_birth = james2_time.pop(0)


print("james2OriData =",james2OriData)
print("james2_time =",james2_time)
print("james2_name =",james2_name)
print("james2_birth =",james2_birth)


#3 整理資料、再取集合(排除重複)，最後取排序
print("\n----------- 一次一個手動來 ----------")
jamesTOP3 = getUnigue(james2_time)[0:3]
print("jamesTOP3 =",jamesTOP3)



print("\n----------- 【變數自動命名】自動做 4 個 ----------")
i=0
for each in nameFourPlayers:
    try:
        locals()["%s"%(each)+"_time"] = locals()["%s"%(each)+"OriData"]
        locals()["%s"%(each)+"_name"] = locals()["%s"%(each)+"_time"].pop(0)
        locals()["%s"%(each)+"_birth"] = locals()["%s"%(each)+"_time"].pop(0)

        locals()["%s"%(each)+"TOP"] = getUnigue(locals()["%s"%(each)+"_time"])[0:3]
        print(each+"TOP =", locals()["%s" % (each)+"TOP"])
        i += 1
    except BaseException as BEerr:
        print("BaseException：",BEerr)





# ===================================================================
print("\n----------- 學習 dict ----------")
# ===================================================================
# 創建
jkDict={}
gameDict=dict()
print("type(jkDict) =",type(jkDict))
print("type(gameDict) =",type(gameDict))
# 添加 (添加的順序 != python維護的順序)
jkDict["J"] = "Jumi"
jkDict["K"] = "KaoChin"
jkDict["Colors"] = ["Red","Yellow","Green","Black","White","Blue"]
gameDict = {"Name":"pad","Android_Rank":[30,2,8,26,12,9]}
# 查找/訪問
print(jkDict["J"])
print(gameDict["Android_Rank"][0:3])
print(sorted(gameDict["Android_Rank"])[0:3])


# ===================================================================
print("\n-------- 【改用dict】改寫代碼 (先一次一個) -------")
# ===================================================================
james2_time = james2OriData
james2_dict = {}
james2_dict["name"] = james2_time.pop(0)
james2_dict["birth"] = james2_time.pop(0)
james2_dict["time"] = james2_time

print("james2OriData =",james2OriData)
print("james2_name =",james2_dict["name"])
print("james2_birth =",james2_dict["birth"])
print("james2_time =",james2_dict["time"])

#3 整理資料、再取集合(排除重複)，最後取排序
jamesTOP3 = getUnigue(james2_dict["time"])[0:3]
print("jamesTOP3 =",jamesTOP3)