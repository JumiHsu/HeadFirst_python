
import os
def changeChdir( bottomPath, fileFolder, txtName ):
    print("當前工作路徑 =",os.getcwd())      # 確認當前的工作路徑

    os.chdir( bottomPath + fileFolder )     # 修改當前工作目錄
    print("變更當前工作路徑後 =",os.getcwd())

    return open(txtName)



bottomPathHome = r"D:\GIT_Tortoise_Jumi_NB\HeadFirst_Python"
bottomPathOffice = r"C:\Users\Jumi_Hsu\Desktop\TortoiseGit_Jumi_jfi\HeadFirst_python"

fileFolder = r"\chapter3"
txtName = "sketch.txt"

sketch = changeChdir(bottomPathOffice, fileFolder, txtName)  # 用之前都要打開
sketckRowNum = len(sketch.readlines())    # txt的資料列數，這邊用完，sketch就消失了



print("\n======== 印出來看一下 ========")
sketch = changeChdir(bottomPathOffice, fileFolder, txtName)  # 用之前都要打開
print(sketch.readline()) # 為什麼這樣可以印出一行!  而且不會關掉檔案
                         # 但會使 txt 的定位點向後移動一行

# 需要使定位點回到第一行
sketch.seek(0)                # 同 tell()



print("\n======== 印出來看一下 ========")
printRowHdFt = 10                          # 只印資料的前後 n 行
lineCount = 0

# sketch = changeChdir(bottomPathOffice, fileFolder, txtName)  # 用之前都要打開
print("\n文檔內容")
for line in sketch:
    lineCount += 1
    if (lineCount <= printRowHdFt) or (lineCount >= sketckRowNum - printRowHdFt):
        print(line)
    elif lineCount == printRowHdFt + 1:
        print("...\n...\n\n")
    else:
        pass
sketch.close              # 先看看文件長怎樣，打開記得關閉





print("\n======== 取得資料，並整理成更好的結構 ========")
sketch = changeChdir(bottomPathOffice, fileFolder, txtName)  # 用之前都要打開
for eachLine in sketch:
    if eachLine.find(":") >0:
        (actor, lineNum) = eachLine.split(": ",1)            # 只對第一個:分隔
        print(actor, end="")
        print(" said: ", end="")
        print(lineNum, end="")
    else:
        pass



# 參考資料：關於讀取指定行
# https://blog.csdn.net/wangdq_1989/article/details/42709853
