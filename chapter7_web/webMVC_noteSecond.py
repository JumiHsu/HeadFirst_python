
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




print("\n=============== 用 dir() 檢查你能做的行為 ===================")
print("dir() =\n",dir(),"\n")

playerPickleTxt = "playerPickle.txt"
playerSaveDict = put_to_store(nameFourPlayers, playerPickleTxt)
playerLoadDict = get_from_store(playerPickleTxt)

print("\n=============== 檢查扔進去的資料 ===================")
for each in playerSaveDict:
    print(playerSaveDict[each].name, playerSaveDict[each].birth,"\n",playerSaveDict[each])

print("\n=============== 檢查取出的資料 ===================")
for each in playerLoadDict:
    print(playerLoadDict[each].name, playerLoadDict[each].birth,"\n",playerLoadDict[each])

