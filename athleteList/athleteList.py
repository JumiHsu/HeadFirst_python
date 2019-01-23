

''' 具有list屬性的運動員class，具備：
    姓名、生日、時間紀錄資料(list)，這三個屬性
'''
class AthleteList(list):
    def __init__(self, playerName, playerBirth=None, playerTime=[]):
        list.__init__([])  # 比之前多做這一步
        self.name = playerName
        self.birth = playerBirth
        self.extend(playerTime)  # self 繼承了 list.extend 這個功能
        self.extendnew = self.extend(playerTime)  # self 繼承了 list.extend 這個功能
        if " " in playerName:
            (self.firstName, self.lastName) = playerName.split(" ", 1)

    def TOP(self, TOPrank):
        return getUnigue(self)[0:TOPrank]  # 這時候的 self 已經是 list 了



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


#function ------ BOOK：讀取原始資料 + 輸出 Athlete 類的 instance ----------
def get_coach_data(filename):
    try:
        with open(filename) as eachfile:
            eachdata = eachfile.readline()
        temp = eachdata.strip().split(",")  # 留意這邊的縮排
        return AthleteList(temp[0], temp[1], temp[2:])
    except IOError as IOerr:
        print("IOError：\n", IOerr, "\n")
    except BaseException as BEerr:
        print("BaseException：\n", BEerr, "\n")



