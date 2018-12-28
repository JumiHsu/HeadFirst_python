

''' 功能：修改工作路徑至指定資料夾，讀取txt檔案

    參數：路徑、檔案filefolder、讀取對象檔名、是否開啟工作路徑檢視
    return：openTxt = open(txtName)
'''

import os
'''
def changechdir_opentxt(btmPath, fileFolder, txtName, cwdCheck=0):
    try:
        if cwdCheck == 0:
            os.chdir(btmPath + fileFolder)  # 僅修改當前工作目錄
        else :
            # 如果想知道工作路徑變化
            print("當前工作路徑 =\n",os.getcwd(),"\n")
            os.chdir(btmPath + fileFolder)
            print("當前工作路徑變更後 =\n", os.getcwd(),"\n")
            openTxt = open(txtName)
        return open(txtName)

    except IOError as IOerr:
        print("IOError：\n{0}\nCheck:\n{1}".format(IOerr, btmPath+fileFolder))
        # return "IOError"
    except BaseException as BEerr:
        print("Something wrong：\n{0}".format(BEerr))
        # return "BaseException"
'''

def changechdir_opentxt(btmPath, fileFolder, txtName, cwdCheck=0):
    try:
        if cwdCheck == 0:
            os.chdir(btmPath + fileFolder)  # 僅修改當前工作目錄
        else:
            # 如果想知道工作路徑變化
            print("當前工作路徑 =\n", os.getcwd(), "\n")
            os.chdir(btmPath + fileFolder)
            print("當前工作路徑變更後 =\n", os.getcwd(), "\n")
        openTxt = open(txtName)
        return openTxt

    except IOError as IOerr:
        print("IOError：\n{0}\nCheck:\n{1}".format(IOerr, btmPath+fileFolder))
        # return "IOError"
    except BaseException as BEerr:
        print("Something wrong：\n{0}".format(BEerr))
        # return "BaseException"



# 字串格式化：https://openhome.cc/Gossip/Python/StringFormat.html
# 路徑格式參考：
# btmPath = r"C:\Users\Jumi_Hsu\Desktop\TortoiseGit_Jumi_jfi\HeadFirst_python"
# btmPath = r"D:\GIT_Tortoise_Jumi_NB\HeadFirst_Python"
# fileFolder = r"\chapter3"
