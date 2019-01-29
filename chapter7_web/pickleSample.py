
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
import openTxt

# 不開檔案，只是單純改工作路徑
def changechdir(btmPath, fileFolder, cwdCheck=0):
    try:
        if cwdCheck == 0:
            os.chdir(btmPath + fileFolder)  # 僅修改當前工作目錄
            print("當前工作路徑變更後 =\n", os.getcwd(), "\n")
        else:
            # 如果想知道工作路徑變化
            print("當前工作路徑 =\n", os.getcwd(), "\n")
            os.chdir(btmPath + fileFolder)
            print("當前工作路徑變更後 =\n", os.getcwd(), "\n")

    except IOError as IOerr:
        print("IOError：\n{0}\nCheck:\n{1}".format(IOerr, btmPath+fileFolder))
    except BaseException as BEerr:
        print("Something wrong：\n{0}".format(BEerr))


# 變更工作路徑
changechdir(btmPath, fileFolder)


print("\n======== 【使用pickle】產生檔案 ========")
PickleSaveTxt = "PickleSaveTxt.txt"
try:
    with open(PickleSaveTxt, "wb") as PickleSave:
        pickle.dump([1,2,3], PickleSave)

except IOError as IOerr:
    print("IOError =", IOerr)
except pickle.PickleError as Perr:
    print("{0}\n{1}".format("PickleError：", Perr))
except BaseException as BEerr:
    print("BaseException Error：\n{0}".format(BEerr))



print("\n======== 【使用pickle】讀檔並列印 ========")
PickleLoadData = []
try:
    with open(PickleSaveTxt, "rb") as PickleLoad:
        PickleLoadData = pickle.load(PickleLoad)

except IOError as IOerr:
    print("{0}\n{1}".format("PickleError：", IOerr))
except pickle.PickleError as Perr:
    print("{0}\n{1}".format("PickleError：", Perr))
except BaseException as BEerr:
    print("BaseException Error：\n{0}".format(BEerr))


print(PickleLoadData)

