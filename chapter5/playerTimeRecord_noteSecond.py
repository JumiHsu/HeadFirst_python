

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


#1 打開txt，讀取資料，並指派給變數
# 想要4個一起讀取，一起處理
txtName_james = "james.txt"
txtName_julie = "julie.txt"
txtName_mikey = "mikey.txt"
txtName_sarah = "sarah.txt"


print("-----------原始資料----------")
AlltxtTerm = [txtName_james, txtName_julie, txtName_mikey, txtName_sarah]
AllRecordList = []

for eachTxt in AlltxtTerm:
    with open(eachTxt) as eachfile:
        eachdata = eachfile.readline()
    eachdataClean = eachdata.strip().split(",")
    AllRecordList.append(eachdataClean)

for i in range(len(AllRecordList)):
    print(AlltxtTerm[i], "=", AllRecordList[i],"\n")



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



#3 排序他們
# 書上教過 list comprehension 後的方式，還可以連帶排序好，也就是
AllRecordCleanSortedList = []
for i in range(len(AllRecordList)):
    temp = sorted( sanitizeString(each) for each in AllRecordList[i] )
    AllRecordCleanSortedList.append(temp)

print("-----------n排序好的四人資料----------")
for i in range(len(AllRecordCleanSortedList)):
    print(AlltxtTerm[i], "=", AllRecordCleanSortedList[i], "\n")



#4 排除重複，找出真正的前三名

# 先做一個人的就好，不要一次四個
jamesRecord = AllRecordCleanSortedList[0]
julieRecord = AllRecordCleanSortedList[1]
mikeyRecord = AllRecordCleanSortedList[2]
sarahRecord = AllRecordCleanSortedList[3]

# 將第一個設定為target，並放入不重複list
# 往後看第二個，比較第二個和target，如果一樣，pass，target不變
# 如果不一樣的話，就放入list，並把第二個設定為target
def deleteRepeat(anyList):
    target = anyList[0]
    NoRepeat = [target]
    for i in range(len(anyList)-1): # 倒數第二個
        if i < len(anyList) :
            if anyList[i+1] == target:
                pass
            else:
                NoRepeat.append(anyList[i+1])
                target = anyList[i+1]
        else:
            pass
    return NoRepeat

jamesNoRepeat = deleteRepeat(jamesRecord)
print("\njamesNoRepeat =",jamesNoRepeat)



# 書上的方法
unigue_james=[]
for i in range(len(jamesRecord)):
    if jamesRecord[i] not in unigue_james:
        unigue_james.append(jamesRecord[i])
    else:
        pass
print("\nunigue =",unigue_james)


# 如果想做很多次
def unigue(anyList):
    unigue=[]
    for i in range(len(anyList)):
        if anyList[i] not in unigue:
            unigue.append(anyList[i])
        else:
            pass
    return unigue

uni_james = unigue(jamesRecord)
uni_julie = unigue(julieRecord)
uni_mikey = unigue(mikeyRecord)
uni_sarah = unigue(sarahRecord)

print("uni_james =",uni_james)
print("uni_julie =",uni_julie)
print("uni_mikey =",uni_mikey)
print("uni_sarah =",uni_sarah)



'''# 學習"集合"
distance = set()
distance = {1,22,44,55,6,7,1}
print(distance) # {1, 6, 7, 44, 22, 55}，順序是為何
'''

james_set=set(jamesRecord)
print("\njames_set =",james_set)



# 綜合利用sorted(),list comprehemsion,set()，快速的抓出前三名
jamesTOP = sorted(
    set([sanitizeString(each) for each in AllRecordList[0]])
    )[0:3]
print("\njamesTOP =",jamesTOP,"\n")


# 動態命名
name=["james","julie","mikey","sarah"]
for i in range(4):
    eachTOP = sorted(set([sanitizeString(each) for each in AllRecordList[i]]))[0:3]
    locals()[ "%s" % (name[i]) +"TOP" ] = eachTOP
    print(  name[i]+"TOP" , "=" , locals()["%s" % (name[i]) + "TOP"] )


# 把整理好的list，輸出成txt
# 參數：路徑、檔案filefolder、讀取對象檔名、是否開啟工作路徑檢視
# try:
#     with open("","rb") as playerTimeRecord:
#         pickle.dump(playerTimeRecord)

