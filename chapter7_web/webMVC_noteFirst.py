
# 上層路徑設定
bottomPathHome = r"D:\GIT_Tortoise_Jumi_NB\HeadFirst_Python"
bottomPathOffice = r"C:\Users\Jumi_Hsu\Desktop\TortoiseGit_Jumi_jfi\HeadFirst_python"

# 檔案夾位置設定
btmPath = bottomPathHome
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
def put_to_store(nameFourPlayers, playerPickleTxt="playerPickle.txt"):
    # ---------------------------
    playerSaveDict = {}
    for each in nameFourPlayers:
        playerSaveDict[each] = athleteList.get_coach_data(each+".txt")

    try:
        with open(playerPickleTxt,"wb") as playerPickleSave:
            pickle.dump(playerSaveDict, playerPickleSave)
        return playerSaveDict
    except IOError as IOerr:
        print("IOError =", IOerr)
    except pickle.PickleError as Perr:
        print("{0}\n{1}".format("PickleError：", Perr))
    except BaseException as BEerr:
        print("BaseException Error：\n{0}".format(BEerr))

    # ---------------------------
    # fileList = ["james.txt", "julie.txt", "mikey.txt", "sarah.txt"]
    # playerSaveDict2 = {}
    # playerPickleTxt = "playerPickle2.txt"
    # for eachFile in fileList:
    #     ath = athleteList.get_coach_data(eachFile)
    #     playerSaveDict2[ath.name] = ath
    # try:
    #     with open(playerPickleTxt,"wb") as playerPickleSave2:
    #         pickle.dump(playerSaveDict2, playerPickleSave2)
    #     return playerSaveDict2
    # except IOError as IOerr:
    #     print("IOError =", IOerr)
    # except pickle.PickleError as Perr:
    #     print("{0}\n{1}".format("PickleError：", Perr))
    # except BaseException as BEerr:
    #     print("BaseException Error：\n{0}".format(BEerr))




'''
讀取檔案 (用pickle)
輸出的時候輸出成 一個長度=4，以名字為key，其值為athleteList class物件的字典
'''
def get_from_store(playerPickleTxt="playerPickle.txt"):
    playerLoadDict = {}
    try:
        with open(playerPickleTxt,"rb") as playerPickleLoad:
            playerLoadDict = pickle.load(playerPickleLoad)
        return playerLoadDict
    except IOError as IOerr:
        print("IOError =", IOerr)
    except pickle.PickleError as Perr:
        print("{0}\n{1}".format("PickleError：", Perr))
    except BaseException as BEerr:
        print("BaseException Error：\n{0}".format(BEerr))




print("dir() =\n",dir(),"\n")
playerPickleTxt = "playerPickle.txt"

print("=============== 檢查扔進去的資料 ===================")
playerSaveDict = put_to_store(nameFourPlayers, playerPickleTxt)
for each in playerSaveDict:
    print(playerSaveDict[each].name, playerSaveDict[each].birth,"\n",playerSaveDict[each],"\n")

print("=============== 檢查取出的資料 ===================")
playerLoadDict = get_from_store(playerPickleTxt)
for each in playerLoadDict:
    print(playerLoadDict[each].name, playerLoadDict[each].birth,"\n",playerLoadDict[each],"\n")



# print("playerSaveDict =",playerSaveDict,"\n")
# print("playerLoadDict =",playerLoadDict,"\n")
# print(playerLoadDict[nameFourPlayers[0]].name)
# print(playerLoadDict[nameFourPlayers[0]].birth)


'''
# open(txt,"rb",encoding="utf8")
# .decode('utf-8').encode('cp950')

1. 不同的操作系统
对于 Windows 系统而言，含有 b（rb、wb、r+b） 表示以二进制形式打开文件。windows 下的 Python 对文本文件（text files）和二进制文件（binary files）的处理方式不同，

2. Python 2 vs Python 3
对于 Python 3 环境：

r：Python 将会按照编码格式进行解析，read() 操作返回的是str
rb：也即 binary mode，read()操作返回的是bytes
--------------------- 
作者：Inside_Zhang 
来源：CSDN 
原文：https://blog.csdn.net/lanchunhui/article/details/55819146 
版权声明：本文为博主原创文章，转载请附上博文链接！

text="cp950"
print(text.encode(sys.stdin.encoding, "replace").decode(sys.stdin.encoding))
'''


# ========================================================================
# 【製作】創建符合 AthleteList類型 的 instance
# ========================================================================
# rank = 3
# for each in nameFourPlayers:
#     locals()["%s" % (each) +
#              "OriData"] = athleteList.get_coach_data(each+".txt")
#     print(each+"OriData =", locals()["%s" % (each) + "OriData"])
#     print(each+"OriData.name =", locals()["%s" % (each) + "OriData"].name)
#     print(each+"OriData.birth =", locals()["%s" % (each) + "OriData"].birth)

#     locals()["%s"%(each) + "TOP" + "%s"%(rank)] = locals()["%s" %
#                                                 (each) + "OriData"].TOP(rank)
#     print(locals()["%s" % (each) + "OriData"].name, "TOP"+str(rank),"=",
#           locals()["%s"%(each) + "TOP" + "%s"%(rank)], "\n")


'''
#1 為什麼Ori本人可以被print，print出來還只有time資料
#2 為什麼.time反而沒東西
#3 寫這樣不對嗎：
# self.time = self.extend(playerTime)
# self.time = playerTime  # 為什麼 PDF P.233(書頁P.208)不用此行

sarahOriData = ['2:58', '2.58', '2:39', '2-25', '2-55', '2:54', '2.18', '2:55', '2:55',
'2:22', '2-21', '2.22']
sarahOriData.name = Sarah Sweeney
sarahOriData.birth = 2002-6-17
sarahOriData.time = None

# 自問自答：
# self 繼承了 list.extend 這個功能，他不必用.time去call
# 等於是 self 本身具備一些可以被呼叫的屬性：name、birth
# 但他自己本身又是一個list，所以要扔 新的timelist的時候，是可以直接扔的
'''
