
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

errorMsg = "發生錯誤，請檢查："



# 打開檔案，並賦值給變數
print("\n打開檔案 ......")
try:
    # sketch = changeChdir(bottomPathOffice, fileFolder, txtName,1)  # 打開檔案
    sketch = changeChdir(bottomPathHome, fileFolder, txtName,1)  # 打開檔案

    sketckRowNum = len(sketch.readlines())  # txt的資料列數
    print("資料列數 =",sketckRowNum)
    
    sketch.close  # 記得關閉
except :  # 這裡不是 IO/Value/TypeError
    print(errorMsg,"無法取得資料列數\n")



print("\n======== 只看一行 ========")
try:
    sketch.seek(0)  # 記得重置定位點
    print(sketch.readline())  # 一次印一行，但會使定位點向後移動一行
except:
    print(errorMsg)



print("\n======== 印出前後 n 行看一下 ========")
try:
    sketch.seek(0)  # 記得重置定位點
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





print("\n======== 【產生file】 ========")
man_data = "man_data.txt"
other_data = "other_data.txt"
try:
    manSpeakList = open( man_data, "w")    # 打開/創建後打開(可寫入)一個文件
    otherSpeakList = open( other_data , "w")

    print( man, file=manSpeakList )        # 用 print 來寫入文件 (why?)
    print(other, file=otherSpeakList)
    # manSpeakList.write(man)              # 不知為何網路上分享的 f.write無用

except :
    print(errorMsg)

finally:
    if "manSpeakList" in locals():
        manSpeakList.close()
    if "otherSpeakList" in locals():
        otherSpeakList.close()








print("\n======== 嘗試開啟一個不存在的檔案1 ========")
try:
    data = open("missing.txt")
    print(data.readline(),end="")
except IOError:
    print("File error")
finally:
    if 'data' in locals():  # 如果有成功開啟，也要記得正常關閉
        data.close()
        print("File close.")





print("\n======== 嘗試開啟一個不存在的檔案2 ========")
print("======== 對於「檔案開啟」一個比較漂亮的結構 ========")
try:
    with open("missing.txt") as data:
        print(data.readline(),end="",file=data)
except IOError:
    print("File error")








print("\n======== 【產生file】使用 with 簡化程式碼 ========")
man2_data = "man2_data.txt"
other2_data = "other2_data.txt"

try:
    with open( man2_data, "w") as man2SpeakList:
        print(man,file=man2SpeakList)
        # nestPrint_home.print_nest_indent_txt(man2SpeakList)

    with open( other2_data, "w") as other2SpeakList:
        print(other,file=other2SpeakList)
        # nestPrint_home.print_nest_indent_txt(other2SpeakList)

except :
    print(errorMsg)





# import sys
# # sys.path.append("C:/Users\Jumi_Hsu\Desktop\TortoiseGit_Jumi_jfi\HeadFirst_python/nestPrint")
# sys.path.append("D:\GIT_Tortoise_Jumi_NB\HeadFirst_Python\nestPrint_home")
import nestPrint_home
import nestPrint

print("\n======== 【產生file】使用 nestPrint，產生兩個新的file ========")
man3_data = "man3_data.txt"
other3_data = "other3_data.txt"
try:
    with open( man3_data, "w") as man3SpeakList:
        nestPrint_home.nestPrintTxt(man,fn=man3SpeakList)

    with open( other3_data, "w") as other3SpeakList:
        nestPrint_home.nestPrintTxt(other,fn=other3SpeakList)

except :
    print(errorMsg)


'''
print("\n======== 這一切都太複雜了，用用看pickle吧 ========")
# 寫入並儲存一個數據
with open('pickleSave.txt',"wb") as mysavedata:
    pickle.dump([1,2,3],mysavedata)

# 讀一個 pickle 儲存過的數據，可以用 load
with open('pickleSave.txt',"rb") as myloaddata:
    pickleLoad = pickle.load(mysavedata)
'''



print("\n======== 【使用pickle】產生檔案 ========")
import pickle
man4_data = "man4_data.txt"
other4_data = "other4_data.txt"
try:
    with open( man4_data, "wb") as man4SpeakList:
        pickle.dump(man,man4SpeakList)

    with open( other4_data, "wb") as other4SpeakList:
        pickle.dump(other,other4SpeakList)

except IOError as err :
    print(errorMsg,"\n",err)
except pickle.PickleError as perr:
    print("PickleError =",perr)
except Exception as Eerr:
    print("Exception Error=",Eerr)

# locals() 會返回當前作用域中，定義的所有名字的一個集合 P.143
# 他會去找，變量名稱為 data 的變量
# 如果有，就會正常close檔案(以避免檔案遺失時，close無法正確呼叫的問題)




print("\n======== 只要新增一點東西，就可以取得error的內容 ========")
try:
    data = open("missing.txt")
    print(data.readline(), end="")

except IOError as err:                  # 可以print出error
    print("File error:",err)
    # print("File error:" + str(err))   # +號只能連接同類型資料
finally:
    if 'data' in locals():
        data.close()


print("\n\n... 但因為try/except/finally實在很常用")
print("所以with可以直接幫你包括 try/finally")
print("以後直接用 try with/except 即可")

print("\n======== [with]嘗試讀取一個不存在的檔案 ========")
try:
    with open("missing.txt") as missingData:
        print(missingData.readline(), end="")
        print("missingData is ...", file=missingData)

except IOError as err:  # 可以print出error
    print("File error:", err)


print("\n======== [with]嘗試讀取一個存在的檔案 ========")
try:
    with open("sketch.txt") as sketchData:  # 若疏忽而加上,"w"，仍會寫入(空白)
        print(sketchData.readline(), end="")  # 這樣可以用open("sketch.txt")

except IOError as err:
    print("File error:", err)


print("\n======== [with]嘗試寫入一個存在的檔案 ========")
try:
    with open("sketchWrite.txt", "w") as sketchWriteData:
        # print(sketchWriteData.readline(), end="")  # 這樣可以用open("sketch.txt")
        print("sketchWrite is ...", file=sketchWriteData)  # 一定要open(".txt","w")

except IOError as err:                  # 可以print出error
    print("File error:", err)


print("\n======== [with]產生兩個新的資料檔案 ========")
man2, other2 = [], []
man2_data = "man2_data.txt"
other2_data = "other2_data.txt"
try:
    sketch.seek(0)                                       # 記得重置定位點
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
    with open(man2_data, "w") as man2SpeakList:  # 打開/創建後打開一個可寫入的文件
        print(man2, file=man2SpeakList)  # 用 print 來寫入文件 (why?)
    with open(other2_data, "w") as other2SpeakList:  # 2個open可用,號連成同一行
        print(other2, file=other2SpeakList)
except IOError as err:
    print(errorMsg,str(err))  # 這邊其實err沒東西 P.147


print("\n======== [with]打開剛剛產生的檔案，看看內容 ========")
try:
    with open(man23_data) as man2Read:
        print(man2Read.readline())
except BaseException as err:  # 用這個描述，可以捕獲所有類型的error
    print("Error:\n{0}".format(err))
    print("{0}\n{1}".format("Error:", err))  # 這兩句顯示起來相同


# 參考資料：

#1 讀取指定行
# https://blog.csdn.net/wangdq_1989/article/details/42709853

#2 讀取檔案的流程相關筆記
# http://www.ttlsa.com/docs/dive-into-python3/files.html

#3 open(f,'mode')的說明
# https://ithelp.ithome.com.tw/articles/10161708

#4 except BaseException as err:
# https://python3-cookbook.readthedocs.io/zh_CN/latest/c14/p07_catching_all_exceptions.html
# 也可以進行自定義異常，切記必須繼承自預設的底層異常class
# BaseException：未必萬用，有時候會因為涵蓋太多種error，而導致該抓的異常沒抓到
