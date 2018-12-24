
import os
def changeChdir( bottomPath, fileFolder, txtName, cwdPrint=0):
    # if os.path.exists(bottomPath + fileFolder + "\\" + txtName):
    # else:
    try:
        if cwdPrint == 0:
            os.chdir(bottomPath + fileFolder)  # 修改當前工作目錄
        else :
            print("\n======== 確認檔案的工作路徑變化 ========")
            print("當前工作路徑 =\n",os.getcwd(),"\n")
            os.chdir( bottomPath + fileFolder )
            print("當前工作路徑變更後 =\n", os.getcwd(),"\n")

        return open(txtName)

        # with open(txtName) as tempFile:
        #     tmpFile = open(txtName)         # 檔案會讀不到，但也不會進 except

        # return tempFile

    except IOError:
        print("Oh!", txtName, "doesn't exit!")
        print("Plz check:\n", bottomPath+fileFolder,"\n")
        return "IOError"

    except:  # 也可寫：(IOError, TypeError, ValueError)
        print("Something Wrong!")
        return "Error"
    
    open(txtName).close





# 檔案路徑設定
bottomPathHome = r"D:\GIT_Tortoise_Jumi_NB\HeadFirst_Python"
bottomPathOffice = r"C:\Users\Jumi_Hsu\Desktop\TortoiseGit_Jumi_jfi\HeadFirst_python"

fileFolder = r"\chapter3"
txtName = "sketch.txt"

errorMsg = "發生錯誤，請檢查!"



# 打開檔案，並賦值給變數
print("\n打開檔案 ......")
try:
    # sketch = changeChdir(bottomPathOffice, fileFolder, txtName,1)  # 打開檔案
    sketch = changeChdir(bottomPathHome, fileFolder, txtName,1)  # 打開檔案
    sketckRowNum = len(sketch.readlines())  # txt的資料列數
    print("資料列數 =",sketckRowNum)
    
    
    sketch.seek(0)  # 因讀到檔案最末行，故定位點移動，需使之回到第一行,同tell()
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
    sketch.seek(0)  # 記得重置定位點
    for eachLine in sketch:
        if eachLine.find(":") >0:
            (actor, lineSpeak) = eachLine.split(": ",1)  # 只對第一個:分隔
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
            print(lineSpeak, end="")  # 不加end，就會多換一次行(why?)
        except:
            # print(eachLine)         # 不加end，就會多換一次行(why?)
            pass                      # 也可以pass，略過整行不印
except:
    print(errorMsg)



print("\n======== 產生兩個新的資料檔案 ========")
man, other = [],[]
man_data = "man_data.txt"
other_data = "other_data.txt"

try:
    sketch.seek(0)  # 記得重置定位點
    for eachLine in sketch:
        try:
            (actor, lineSpeak) = eachLine.split(":", 1)  # 只對第一個: 分隔
            lineSpeak = lineSpeak.strip()                # 清除頭尾垃圾
            if actor == "Man" or actor == "man":
                man.append(lineSpeak)
            else:
                other.append(lineSpeak)

        except:
            # print(eachLine)                 # 不加end，就會多換一次行(why?)
            pass                              # 也可以pass，略過整行不印
    
    print("man的台詞 =", man, "\n共有幾句=", len(man))
    print("\n其他人的台詞 =", other, "\n共有幾句=", len(other))

except:
    print(errorMsg)


try:
    manSpeakList = open( man_data, "w")    # 打開/創建後打開(可寫入)一個文件
    otherSpeakList = open( other_data , "w")

    print( man, file=manSpeakList )        # 用 print 來寫入文件 (why?)
    print(other, file=otherSpeakList)
    # manSpeakList.write(man)              # 不知為何網路上分享的 f.write無用

except :
    print(errorMsg)

finally:
    manSpeakList.close()
    otherSpeakList.close()



print("\n======== 對於「檔案開啟」一個比較漂亮的結構 ========")
print("\n======== 嘗試開啟一個不存在的檔案 ========")
try:
    data = open("missing.txt")
    print(data.readline(),end="")

except IOError:
    print("File error")
finally:
    if 'data' in locals():  # 如果有成功開啟，也要記得正常關閉
        data.close()
        print("File close.")







print("\n======== 使用 nestPrint，產生兩個新的file ========")
man2, other2 = [],[]
man2_data = "man2_data.txt"
other2_data = "other2_data.txt"

try:
    sketch.seek(0)  # 記得重置定位點
    for eachLine in sketch:
        try:
            (actor, lineSpeak) = eachLine.split(":", 1)  # 只對第一個: 分隔
            lineSpeak = lineSpeak.strip()                # 清除頭尾垃圾
            if actor == "Man" or actor == "man":
                man2.append(lineSpeak)
            else:
                other2.append(lineSpeak)

        except:
            # print(eachLine)                 # 不加end，就會多換一次行(why?)
            pass                              # 也可以pass，略過整行不印
    
    print("man的台詞 =", man2, "\n共有幾句=", len(man2))
    print("\n其他人的台詞 =", other2, "\n共有幾句=", len(other2))

except:
    print(errorMsg)


try:
    manSpeakList = open( man2_data, "w")    # 打開/創建後打開(可寫入)一個文件
    otherSpeakList = open( other2_data , "w")

    print(man2, file=manSpeakList)        # 用 print 來寫入文件 (why?)
    print(other2, file=otherSpeakList)

except :
    print(errorMsg)

finally:
    manSpeakList.close()
    otherSpeakList.close()






# 參考資料：

#1 讀取指定行
# https://blog.csdn.net/wangdq_1989/article/details/42709853

#2 讀取檔案的流程相關筆記
# http://www.ttlsa.com/docs/dive-into-python3/files.html

#3 open(f,'mode')的說明
# https://ithelp.ithome.com.tw/articles/10161708
