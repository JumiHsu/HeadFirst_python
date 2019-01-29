'''心得
1.把例外格式的資料用pop取出
2.使用 dict 管理不同格式的資料
3.如果不想動到原始資料，使用 copy.deepcopy
4.也可以改用 new = old[:] 來實現 deepcopy (slice)
5.將這整件事，定義成一個class
6.其實你不用在def中，動態生成變數名稱，你扔出他本人就好 (除非是為了提高可讀性)
7.妥善運用函式化的寫法，讓程式碼更簡潔：newList = [fc(each) for each in oldList]
8.如果你想對 class的 原始time資料 追加東西，
  請將此動作設定成class裡面的一個fun (Objnew.timeadd("1.21"))
  而不是叫出 Objnew.time 之後才去append (Objnew.time.append("1.21"))
PS. P.198問答的最後一段不懂
9. list1.extend(list2) = list 1+2
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
# nameFourPlayers[0]+".txt"
print("nameFourPlayers =", nameFourPlayers, "\n")




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


#function --------- getUnigue(髒timeList) = 乾淨 + 已排序的timeList ------------
def getUnigue(playertimeList):
    unigueSet = sorted(set([sanitizeString(each) for each in playertimeList]))
    return unigueSet




class Athlete:
    # 定義這個class，可以被什麼指令call出，以及定義這些東西，他會被傳入什麼
    def __init__(self, playerName, playerBirth=None, playerTime=[]):
        self.name = playerName
        self.birth = playerBirth
        self.time = playerTime
        if " " in playerName:
            (self.firstName, self.lastName) = playerName.split(" ",1)

    # 函數：你可以任意使用 __init__定義過的物件，搭配其他新增的參數
    def TOP(self, TOPrank):
        return getUnigue(self.time)[0:TOPrank]

    def addTime(self, singleTime):
        return self.time.append(str(singleTime))

    def addTimes(self, listTime):
        # for each in listTime:
        #     self.time.append(str(each))
        # return self.time
        newlistTime = [str(each) for each in listTime] #self.time的元素須是字串(by getUnigue)
        return self.time.extend(newlistTime)


#function ------ BOOK：讀取原始資料 + 輸出 Athlete 類的 instance ----------
def get_coach_data(filename):
    try:
        with open(filename) as eachfile:
            eachdata = eachfile.readline()
        temp = eachdata.strip().split(",")  # 留意這邊的縮排
        return Athlete(temp[0], temp[1], temp[2:])
    except IOError as IOerr:
        print("IOError：\n", IOerr, "\n")
    except BaseException as BEerr:
        print("BaseException：\n", BEerr, "\n")




# ========================================================================
# 【製作】創建符合 Athlete類型 的 instance
# ========================================================================
print("\n------- 【方案二】創建符合 Athlete類型 的 instance ------")
for each in nameFourPlayers:
    rank = 3
    locals()["%s" % (each) + "OriData"] = get_coach_data(each+".txt")
    locals()["%s" % (each) + "TOP3"] = locals()["%s" % (each) + "OriData"].TOP(rank)
    # print(each+"TOP3 =", locals()["%s" % (each) + "TOP3"], "\n")
    print(locals()["%s" % (each) + "OriData"].name, "TOP3 =",  # 改成直接用 obj.name去呼叫
          locals()["%s" % (each) + "TOP3"], "\n")


#class ------------- BOOK ------------------------
# 使用方式：
# 指派：newObj = Athlete("姓名","生日","時間list")，self 就是 newObj
# 這時候就會針對 newObj 這個物件，產生三個可被呼叫的 物件屬性：
# newObj.name = 姓名
# newObj.birth = 生日
# newObj.time = 時間list
# 所以你可以令 something = newObj.time ，那something就會是一個list
# 你也可以針對其中的某些物件屬性，去做相關的函數運算，比如 newObj.TOP(3)
