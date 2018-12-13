
import os
def changeChdir( bottomPath, fileFolder, txtName, cwdPrint=0):
    # if os.path.exists(bottomPath + fileFolder + "\\" + txtName):
    # else:
    try:
        if cwdPrint == 0:
            os.chdir(bottomPath + fileFolder)           # 修改當前工作目錄
        else :
            print("\n======== 確認檔案的工作路徑變化 ========")
            print("當前工作路徑 =\n",os.getcwd(),"\n")   # 確認當前的工作路徑
            os.chdir( bottomPath + fileFolder )         # 修改當前工作目錄
            print("當前工作路徑變更後 =\n", os.getcwd(),"\n")

        return open(txtName)

        # with open(txtName) as tempFile:
        #     tmpFile = open(txtName)         # 檔案會讀不到，但也不會進 except

        # return tempFile

    except IOError:
        print("Oh!", txtName, "doesn't exit!")
        print("Plz check:\n", bottomPath+fileFolder,"\n")
        return "IOError"

    except:                        # 也可寫：(IOError, TypeError, ValueError)
        print("Something Wrong!")
        return "Error"
    
    open(txtName).close


'''
with open('examples/chinese.txt', encoding='utf-8') as a_file:
    a_file.seek(17)
    a_character = a_file.read(1)
    print(a_character)
'''




bottomPathHome = r"D:\GIT_Tortoise_Jumi_NB\HeadFirst_Python"
bottomPathOffice = r"C:\Users\Jumi_Hsu\Desktop\TortoiseGit_Jumi_jfi\HeadFirst_python"

fileFolder = r"\chapter3"
txtName = "sketch.txt"

errorMsg = "發生錯誤，請檢查!"



print("\n打開檔案 ......")
try:
    sketch = changeChdir(bottomPathOffice, fileFolder, txtName,1)  # 打開檔案
    sketckRowNum = len(sketch.readlines())  # txt的資料列數
                                            # 因讀到檔案最末行，故定位點移動到最末
    print("資料列數 =",sketckRowNum)
    sketch.seek(0)                          # 同 tell()，需要使定位點回到第一行
    # sketch.close                          # 記得關閉
except :                                    # 這裡不能用 IO/Value/TypeError
    print(errorMsg,"無法取得資料列數\n")



print("\n======== 只看一行 ========")
try:
    print(sketch.readline())                # 一次印一行，但會使定位點向後移動一行
except:
    print(errorMsg)



print("\n======== 印出前後 n 行看一下 ========")
try:
    sketckRowNum = len(sketch.readlines())  # txt的資料列數
    printRowHdFt = 3                        # 只印資料的前後 n 行
    lineCount = 0
    
    sketch.seek(0)                          # 同 tell()，需要使定位點回到第一行
    for line in sketch:
        lineCount += 1
        if (lineCount <= printRowHdFt) or (lineCount >= sketckRowNum - printRowHdFt):
            print(line)
        elif lineCount == printRowHdFt + 1:
            print("...\n...\n\n")
        else:
            pass
except:                                     # 這裡不能用 IOError/ValueError
    print(errorMsg)






print("\n======== 取得資料，並整理成更好的結構 ========")
try:
    sketch.seek(0)                                            # 記得重置定位點
    for eachLine in sketch:
        if eachLine.find(":") >0:
            (actor, lineSpeak) = eachLine.split(": ",1)       # 只對第一個:分隔
            print(actor, end="")
            print(" said: ", end="")
            print(lineSpeak, end="")
        else:
            pass
except:
    print(errorMsg)



print("\n======== 總不能遇到問題就處理吧(說啥呢) ========")
print("假設我們不處理特殊的符號問題")
# if isinstance(sketch, str):
#     print(sketch)
# else:
try:
    sketch.seek(0)                                       # 記得重置定位點
    for eachLine in sketch:
        try:
            (actor, lineSpeak) = eachLine.split(": ",1)  # 只對第一個: 分隔
            print(actor, end="")
            print(" said: ", end="")
            print(lineSpeak, end="")                # 不加end，就會多換一次行(why?)
        except:
            # print(eachLine)                       # 不加end，就會多換一次行(why?)
            pass                                    # 也可以pass，略過整行不印
except:
    print(errorMsg)




print("\n======== 代碼磁貼 ========")

man = []
other = []
try:
    sketch.seek(0)                                       # 記得重置定位點
    for eachLine in sketch:
        try:
            (actor, lineSpeak) = eachLine.split(":", 1)  # 只對第一個: 分隔
            lineSpeak = lineSpeak.strip()                # 清除頭尾垃圾
            # lineSpeak = lineSpeak.replace("","")       # 清除頭尾垃圾
            if actor == "Man" or actor == "man":
                man.append(lineSpeak)
            else:
                other.append(lineSpeak)

        except:
            # print(eachLine)                       # 不加end，就會多換一次行(why?)
            pass                                    # 也可以pass，略過整行不印
    
    print("man的台詞 =", man, "\n共有幾句=", len(man))
    print("\n其他人的台詞 =", other, "\n共有幾句=", len(other))

except:
    print(errorMsg)


try:

    
    man_data = "man_data.txt"
    other_data = "other_data.txt"

    manSpeakList = open( man_data, "w")       # 打開/創建後打開(可寫入)一個文件
    print( man, file=manSpeakList )           # 用 print 來寫入文件 (why?)
    # manSpeakList.write(man)

    otherSpeakList = open( other_data , "w")
    print(other, file=otherSpeakList)
    # otherSpeakList.write(other)

    manSpeakList.close()
    otherSpeakList.close()

except :
    print(errorMsg)




# out = open(txtName,"w")
# print("out=",out)
# print("aaaaaaaaaaaaaaaa",file=out)   # 他寫入，是移除整個內容後，才寫入新的
# print("out=", out)

# print("\n======== OUT ========")
# try:
#     for eachLine in out:
#         print(eachLine)
# except:
#     print(errorMsg)
# out.close()




# 參考資料：

#1 讀取指定行
# https://blog.csdn.net/wangdq_1989/article/details/42709853

#2 讀取檔案的流程相關筆記
# http://www.ttlsa.com/docs/dive-into-python3/files.html

#3 open(f,'mode')的說明
# https://ithelp.ithome.com.tw/articles/10161708
