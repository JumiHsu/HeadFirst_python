'''心得
1.把例外格式的資料用pop取出
2.使用 dict 管理不同格式的資料
3.如果不想動到原始資料，使用 copy.deepcopy
4.也可以改用 new = old[:] 來實現 deepcopy (slice)
'''

# 上層路徑設定
bottomPathHome = r"D:\GIT_Tortoise_Jumi_NB\HeadFirst_Python"
bottomPathOffice = r"C:\Users\Jumi_Hsu\Desktop\TortoiseGit_Jumi_jfi\HeadFirst_python"

# 檔案夾位置設定
nowPath = bottomPathOffice
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
print("nameFourPlayers =", nameFourPlayers,"\n")


#function ------------- 讀取 原始資料 ------------------------
def get_playerData(filename):
    try:
        with open(filename) as eachfile:
            eachdata = eachfile.readline()
            locals()["%s" % (each) + "OriData"] = eachdata.strip().split(",")
            # print("\n",each+"OriData =", locals()["%s" % (each) + "OriData"])
            return locals()["%s" % (each) + "OriData"]
    except IOError as IOerr:
        print("IOError：\n", IOerr, "\n")
    except BaseException as BEerr:
        print("BaseException：\n", BEerr, "\n")


#function ------------- 製作 dict ------------------------
def makeDict_playerData(playerRecList, each):
    try:
        # 丟進去的是，含有姓名、生日、時間的複合list
        locals()["%s" % (each)+"_dict"] = {}
        locals()["%s" % (each)+"_dict"]["name"] = playerRecList[0]
        locals()["%s" % (each)+"_dict"]["birth"] = playerRecList[1]
        timeDataLength = len(playerRecList)-2
        locals()["%s" % (each)+"_dict"]["time"] = playerRecList[2:timeDataLength]

        print("\n",each+"_dict =", locals()["%s" % (each)+"_dict"], "\n")

        return locals()["%s" % (each)+"_dict"]

    except IOError as IOerr:
        print("IOError：\n", IOerr, "\n\n")
    except BaseException as BEerr:
        print("BaseException：\n", BEerr, "\n\n")


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
    (min, sec) = timeString.split(splitter)
    return (min + "." + sec)


#function ------------ 整理資料、再取集合(排除重複)，最後取"由小至大"排序 ---------------
def getUnigue(playertimeList):
    unigueSet = sorted(set([sanitizeString(each) for each in playertimeList]))
    return unigueSet




# ===================================================================
# ===================================================================
#1 讀取 原始資料 + 製作 dict
for each in nameFourPlayers:
    locals()["%s" % (each) + "OriData"] = get_playerData(each+".txt")
    tempRecList = locals()["%s" % (each) + "OriData"]
    locals()["%s" % (each)+"_dict"] = makeDict_playerData(tempRecList, each)




# ===================================================================
print("\n-------- 【用slice】【變數自動命名】自動做 4 個  -------")
# ===================================================================
i = 0
for each in nameFourPlayers:
    try:
        locals()["%s" % (each)+"TOP3"] = getUnigue(locals()
                                                    ["%s" % (each)+"_dict"]["time"])[0:3]
        print(locals()["%s" % (each)+"_dict"]["name"],
              "TOP3 =", locals()["%s" % (each)+"TOP3"])
        i += 1
    except BaseException as BEerr:
        print("BaseException：", BEerr)


# ===================================================================
print("\n-------- 【學習使用class】P.215  -------")
# ===================================================================
class practice:
    def __init__(self, value=0):
        # the code to initialize a "practice" object
        self.thing = value

    def how_long(self):  # how_long：是一個方法
        print("self.thing =", self.thing)
        return len(self.thing)


a = practice()
# 等同 practice().__init__(a)
# 也等同 super().__init__(*args, **kwargs)
# practice=類(class)，init=方法(method)，a=實例(instance)
# 也等同 super().__init__(*args, **kwargs)

b = practice("Im JUMI.")
b.how_long()

class Athlete:
    def __init__(self, a_name, a_birth=None, a_times=[]):
        self.name = a_name
        self.birth = a_birth
        self.times = a_times

# 創建符合 Athlete類型 的
sarah = Athlete(sarah2OriData[0], sarah2OriData[1],
                sarah2OriData[2:len(sarah2OriData)-2])

james = Athlete(james2OriData[0], james2OriData[1],
                james2OriData[2:len(james2OriData)-2])

print(type(sarah))
print(type(james))

print(sarah.name)
print(sarah.birth)
print(sarah.times)
