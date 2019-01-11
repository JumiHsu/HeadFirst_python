

# 上層路徑設定
bottomPathHome = r"D:\GIT_Tortoise_Jumi_NB\HeadFirst_Python"
bottomPathOffice = r"C:\Users\Jumi_Hsu\Desktop\TortoiseGit_Jumi_jfi\HeadFirst_python"

# 檔案夾位置設定
nowPath = bottomPathOffice
fileFolder = r"\chapter5"

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

# 變更工作路徑
openTxt.changechdir(nowPath, fileFolder)


# 打開txt，讀取資料，並賦值給變數
txtName_james = "james.txt"
txtName_julie = "julie.txt"
txtName_mikey = "mikey.txt"
txtName_sarah = "sarah.txt"


#1 ==================== 寫法一 ====================
# To do:如何正確關閉檔案，jamesData.close無作用
jamesData = openTxt.changechdir_opentxt(nowPath, fileFolder, txtName_james)

# To do:看一下這份資料再處理

# 檢查資料格式，整理乾淨，放進list
jamesData.seek(0)
for eachline in jamesData:
    jamesTimeRecord = eachline.strip().split(",")
print("\n[寫法一]jamesTimeRecord =\n", jamesTimeRecord,"\n-----------------")



#2 ==================== 寫法二 ====================
with open(txtName_james) as jamesfile:
    jamesData = jamesfile.readline()
jamesTimeRecord = jamesData.strip().split(",")  # split完會是一個list

print("\n[寫法一]jamesTimeRecord =\n", jamesTimeRecord,"\n-----------------")

'''
#3 ==================== 錯誤寫法 ====================
# 他只有一列，split完之後已經是list了
jamesDataClean = []
jamesData.seek(0)
for eachline in jamesData:
    jamesTimeRecord = eachline.strip().split(",")
jamesDataClean.append(jamesTimeRecord)
print("\njamesDataClean=", jamesDataClean)
'''


print("-----------想要依次印出5個檔案，分別指派給5個不同的變數----------")
AlltxtTerm = [txtName_james, txtName_julie, txtName_mikey, txtName_sarah]
AllRecordList = []

for eachTxt in AlltxtTerm:
    with open(eachTxt) as eachfile:
        eachdata = eachfile.readline()
    eachdataClean = eachdata.strip().split(",")
    AllRecordList.append(eachdataClean)

for i in range(len(AllRecordList)):
    print(AlltxtTerm[i], "=", AllRecordList[i],"\n")


#1整理資料 ------------ 符號取代 ------------
def sanitizeList(timeList):
    cleantimeList=[]
    for eachTimeRecord in timeList:
        cleanTemp = eachTimeRecord.replace(":", ".")  # replace會返回一個值
        cleanTemp = cleanTemp.replace("-", ".")
        cleanTemp = cleanTemp.replace(",", ".")
        cleantimeList.append(cleanTemp)
    return cleantimeList

AllRecordCleanList = []
for i in range(len(AllRecordList)):
    AllRecordCleanList.append(sanitizeList(AllRecordList[i]))


#2整理資料 ------------ 把分、秒"分開"來 ------------
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

AllRecordCleanList2 = []
for eachRecord in AllRecordList:
    eachRecordtemp = []
    for eachTime in eachRecord:
        eachRecordtemp.append(sanitizeString(eachTime))
    AllRecordCleanList2.append(eachRecordtemp)




# sort這個list，找出前三名
'''
list.sort():原地排序
listCopy=sorted(list):會複製一個再排序
'''
print("1----------- 一次對這五個資料，排序，並列印出來 ----------")
AllRecordSortedList = []
for i in range(len(AllRecordCleanList)):
    AllRecordSortedList.append(sorted(AllRecordCleanList[i]))

for i in range(len(AllRecordSortedList)):
    print(AlltxtTerm[i], "=", AllRecordSortedList[i], "\n")


print("2----------- 一次對這五個資料，排序，並列印出來 ----------")
AllRecordSortedList2 = []
for i in range(len(AllRecordCleanList2)):
    AllRecordSortedList2.append(sorted(AllRecordCleanList2[i]))

for i in range(len(AllRecordSortedList2)):
    print(AlltxtTerm[i], "=", AllRecordSortedList2[i], "\n")


# 把整理好的list，輸出成txt
# 參數：路徑、檔案filefolder、讀取對象檔名、是否開啟工作路徑檢視
# try:
#     with open("","rb") as playerTimeRecord:
#         pickle.dump(playerTimeRecord)
