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
nowPath = bottomPathOffice
fileFolder = r"\chapter5"

# 匯入modual
import os
import sys
import pickle  # 需要讀檔+輸出檔案時可以用
sys.path.append(nowPath + "/openTxt")
import openTxt

# 變更工作路徑
openTxt.changechdir(nowPath, fileFolder)


print("----------- 定義 預計會常用到的的關鍵字 ----------")
nameFourPlayers = ["james", "julie", "mikey", "sarah"]
txtFourPlayers = [str(each) + ".txt" for each in nameFourPlayers]
oriFourPlayers = [str(each) + "OriData" for each in nameFourPlayers]
print("nameFourPlayers =", nameFourPlayers)
print("txtFourPlayers =", txtFourPlayers)
print("oriFourPlayers =", oriFourPlayers)


#1 打開並讀取txt，並指派給變數，
# 額外把四筆ori資料，塞進一個list
print("\n----------- 原始資料 ----------")
oriReadData = []
for each in nameFourPlayers:
    try:
        with open(each+".txt") as eachfile:
            eachdata = eachfile.readline()
            locals()["%s"%(each) + "OriData"] = eachdata.strip().split(",")
            print(each+"OriData =", locals()["%s" % (each) + "OriData"], "\n")

            oriReadData.append(locals()["%s" % (each) + "OriData"])
    except IOError as IOerr:
        print("IOError：\n",IOerr, "\n")
    except BaseException as BEerr:
        print("BaseException：\n", BEerr, "\n")

# 這樣寫會報錯
# oriReadData = [locals()["%s" % (each)] for each in oriFourPlayers]
print("oriReadData =", oriReadData)



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


#3 整理資料、再取集合(排除重複)，最後取排序
print("\n----------- 一次一個手動來 ----------")
jamesTOP3 = getUnigue(jamesOriData)[0:3]
print("jamesTOP3 =",jamesTOP3)


# 要丟進 getUnigue 的是 locals()["%s" % (each) + "OriData"]
# 也就是 oriReadData[i]
print("\n----------- 【先把資料放進list】自動做 4 個 ----------")
i = 0
for each in nameFourPlayers:
    try:
        locals()["%s" % (each)+"TOP3"] = getUnigue(oriReadData[i])[0:3]
        print(each+"TOP3 =", locals()["%s" % (each)+"TOP3"])
        i += 1
    except BaseException as BEerr:
        print("BaseException：", BEerr)


print("\n----------- 【變數自動命名】自動做 4 個 ----------")
i=0
for each in nameFourPlayers:
    try:
        locals()["%s"%(each)+"TOP"] = getUnigue(locals()["%s"%(each)+"OriData"])[0:3]
        print(each+"TOP =", locals()["%s" % (each)+"TOP"])
        i += 1
    except BaseException as BEerr:
        print("BaseException：",BEerr)



# 把整理好的list，輸出成txt
# 參數：路徑、檔案filefolder、讀取對象檔名、是否開啟工作路徑檢視
# try:
#     with open("","rb") as playerTimeRecord:
#         pickle.dump(playerTimeRecord)

