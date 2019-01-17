'''心得
1.把例外格式的資料用pop取出
2.使用 dict 管理不同格式的資料
3.如果不想動到原始資料，使用 copy.deepcopy
4.也可以改用 new = old[:] 來實現 deepcopy (slice)
5.將這整件事，定義成一個class
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
            return eachdata.strip().split(",")
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
        timeDataLength = len(playerRecList)-2  # timeDataLength=12,但應填14,why
        # locals()["%s" % (each)+"_dict"]["time"] = playerRecList[2:timeDataLength]
        locals()["%s" % (each)+"_dict"]["time"] = playerRecList[2:]

        print("\n",each+"_dict =", locals()["%s" % (each)+"_dict"], "\n")

        return locals()["%s" % (each)+"_dict"]  #, timeDataLength

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





# ========================================================================
#1 讀取 原始資料 + 製作 dict
# ========================================================================
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





# ========================================================================
#2 因為已經獲得了 dict 資料，所以可以針對 Athlete資料 的處理，製作一個 class
# ========================================================================
# 使用方式：
# 指派：newObj = Athlete("姓名","生日","時間list")，self 就是 newObj
# 這時候就會針對 newObj 這個物件，產生三個可被呼叫的 物件屬性：
# newObj.name = 姓名
# newObj.birth = 生日
# newObj.time = 時間list
# 所以你可以令 something = newObj.time ，那something就會是一個list
# 你也可以針對其中的某些物件屬性，去做相關的函數運算，比如 newObj.TOP(3)

class Athlete:
    # 定義這個class，可以被什麼指令call出，以及定義這些東西，他會被傳入什麼
    def __init__(self, playerName, playerBirth=None, playerTime=[]):
        self.name = playerName
        self.birth = playerBirth
        self.time = playerTime
        (self.firstName, self.lastName) = playerName.split(" ")
    
    # 函數：你可以任意使用 __init__定義過的物件，搭配其他新增的參數
    def TOP(self, TOPrank):
        return getUnigue(self.time)[0:TOPrank]

    # def TOP(self, TOPrank):
    #     try:
    #         locals()["%s" % (self.firstName)+"TOP"+str(TOPrank)
    #                  ] = getUnigue(self.time)[0:3]
    #         print(self.firstName+"TOP"+str(TOPrank),
    #               "=", locals()["%s" % (self.firstName)+"TOP"+str(TOPrank)])

    #         return locals()["%s" % (self.firstName)+"TOP"+str(TOPrank)]
    #     except BaseException as BEerr:
    #         print("BaseException：", BEerr)
    #         pass





# ===================================================================
# 3 創建符合 Athlete類型 的 instance
# ===================================================================
print("\n------------- 創建符合 Athlete類型 的 instance ---------")
i = 0
for each in nameFourPlayers:
    # 要傳進去 class 的參數
    FullName = locals()["%s" % (each)+"_dict"]["name"]
    birth = locals()["%s" % (each)+"_dict"]["birth"]
    uniguetime = getUnigue(locals()["%s" % (each)+"_dict"]["time"])  # 記得整理資料

    rank = 3
    locals()["player_"+"%s" % (each)] = Athlete(FullName, birth, uniguetime)
    '''
    print("player_"+each, "=", locals()["player_"+"%s" % (each)].name,
                            locals()["player_"+"%s" % (each)].birth,
                            locals()["player_"+"%s" % (each)].time)'''

    locals()["%s" % (each)+"TOP"+str(rank)] = locals()["player_"+"%s" % (each)].TOP(rank)
    # print(each+"TOP"+str(rank),"=",locals()["%s" % (each)+"TOP"+str(rank)],"\n")







'''
# Last Name = Family Name = 姓
# First Name = Given Name = 名
jumi = "Jumi hsu"
(FirstName, LastName) = jumi.split(" ")
print("FirstName =", FirstName)
print("LastName =", LastName)
'''

'''
class practice:
    def __init__(self, value=0):
        # the code to initialize a "practice" object
        self.thing = value

    def how_long(self, num):  # how_long：是一個方法
        print("self.thing =", self.thing, "    num =", num)
        return len(self.thing)

a = practice()
# 等同 practice().__init__(a)
# 也等同 super().__init__(*args, **kwargs)
# practice=類(class)，init=方法(method)，a=實例(instance)
# 也等同 super().__init__(*args, **kwargs)

b = practice("Im JUMI.")
b.how_long(2)
'''
