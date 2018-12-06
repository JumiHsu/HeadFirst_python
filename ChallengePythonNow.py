
# https://pythonhow.com/start/
questionNo = 0

# Level 1
# What’s the 101st character of the text?
target = "Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient python, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, baxa quouq. axa la consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Proin at neque et tellus ultricies consequat. Duis vitae mi commodo, suscipit nunc vel, porta tellus. In eu volutpat sapien. Mauris dignissim velit eget diam tristique, nec egestas magna maximus. Pellentesque python, lorem a eleifend vehicula, arcu urna facilisis odio, maximus maximus massa nisl sed sapien. Quisque nisi nunc, dignissim ut malesuada non, fringilla vitae sem. Nunc turpis quam, rutrum at egestas ut, pretium tincidunt est. Praesent imperdiet mauris eu felis lobortis vehicula. Sed dictum lorem at rutrum rhoncus. Suspendisse sit amet ex ac eros python cursus. Duis pretium rutrum lacus, sit amet vulputate ipsum condimentum vel. Vivamus lacus ipsum, python in justo quis, blandit condimentum velit esed semper posuere leo, elementum tristique leo euismod quis."
questionNo += 1
print("\n",questionNo,".",target[100])




# https://pythonhow.com/start/t
# Level 2
# 承上，The middle character
# middle = 奇數時，位置=除2取整+1，但字串從0起算，所以位置=除2取整
questionNo += 1
if len(target)%2 == 0:
    print("\n",questionNo,".","plz Check.")
else:
    print( "\n",questionNo,".",target[ int(len(target)/2) ] )



# https://pythonhow.com/start/x
# Level 3
# 承上，The three middle character，中間三個字符
questionNo += 1
takeNum = 3
halfNum = int(takeNum/2)
print("\n",questionNo,".",
    target[
        int(len(target)/2)-halfNum :
        int(len(target)/2)+halfNum+1
        ]
        )
''' Tip
text="1234567"
print( text[2 : 5] )
print(int(len(text)/2)-halfNum) # 中間位置 - 取整(取用字符數/2) = 開始位置
print(int(len(text)/2)+halfNum) # 中間位置 + 取整(取用字符數/2) = 結束位置
# 但因為他取左不取右，所以要 + 1
print(int(len(text)/2)+halfNum+1) # 中間位置 + 取整(取用字符數/2)+1
'''

# https://pythonhow.com/start/axa
# Level 4
# 承上，先獲得此文章總字數，
# 並藉由 0->a, 1->b, ...的字符轉換關係，取得下一階段關鍵字
questionNo += 1

targetCharacterTotal = len(target)
targetCharacterTotalStr = str(targetCharacterTotal)
print("\n文章總長度 =",targetCharacterTotal)

alphabetSmallList = [chr(k) for k in range(97,122)]
print("alphabetSmallList =",alphabetSmallList)


# ============================================================
# 數字轉字母
# ============================================================
def changeKeyword(keyNum):
    index = 0
    ans=[]
    keyNumStr = str(keyNum)
    while index < len(keyNumStr):
        ans.append( alphabetSmallList[ int(keyNumStr[index]) ] )
        index += 1
    return "".join(ans)
# 63:TypeError
# list indices must be integers or slices, not str
# 解決： targetCharacterTotalStr[index]為一個str，但規格為 list[int]

ans4 = changeKeyword(targetCharacterTotalStr)

print("\n",questionNo,".",ans4)





''' 生成 List、Dict '''
serial1 =[k for k in range(0,26)]    # 一個list
serial2 ={k for k in range(0,26)}    # 結果他是一個set，不是dict
serial3 = dict.fromkeys(serial1, 0)                   # 這樣才是一個dict
serial4 = dict.fromkeys([k for k in range(0,26)], 0)  # 這樣才是一個dict
# print("serial4=",serial4,type(serial4))

''' 生成字母表，ASCII碼表，Dec碼為10進位碼 '''
ASCII=[]
for j in range(65,91):                # 寫法 1 = ['A', 'B', 'C',..., 'Z']
    ASCII.append(chr(j))

[chr(j) for j in range(97,123)]       # 寫法 2 = ['a', 'b', 'c',..., 'z']



''' 生成連續字串，用 "".join 就可以串在一起 '''
"".join( [chr(j) for j in range(65,91)] )   # 寫法 1 = ABCDEFG...WXYZ


''' string.ascii_lowercase本身就是連續字串 '''
import string
# print("string.ascii_lowercase =",string.ascii_lowercase)  # 寫法 2 = ab...xyz


''' 生成字典，直接取用 import string  '''
import string
for j in range(0,26):
    serial3[j] = string.ascii_lowercase[j]
# print("\nserial3 =",serial3)

''' 生成字典，直接取用 import string (但統一都被填入0)'''
dict.fromkeys(string.ascii_lowercase, 0)
# print("\ndict.fromkeys =",dict.fromkeys(string.ascii_lowercase, 0))






# https://pythonhow.com/start/bjbh
# Level 5
# 承上，找出這篇文章有幾個詞，並且此數字轉換為字母
questionNo += 1


# ============================================================
# 字串清理
# ============================================================
def strClean(anystr):
    targetClean = anystr.strip()                    # 先清除頭尾垃圾
    targetClean = targetClean.replace(",","")
    targetClean = targetClean.replace(".","")       # 清除一些非屬單詞的符號
    if targetClean.find("  ") > 0 :                 # 整理雙空白
        targetClean = targetClean.replace("  "," ")
    else:
        pass
    return targetClean

targetClean = strClean(target)
wordTotal = targetClean.count(" ") + 1          # 計算空白出現次數 +1
print("wordTotal =" ,wordTotal)
# print("第一個出現位置 =",(target.find(" ")))   # 這是針對字串找位置

ans5 = changeKeyword(wordTotal)
print("\n",questionNo,".",ans5)

''' 如果有連續4空白，會 4 → 2+1 → 1+1=2 
test = "AA B    C D E  F  G H  "   # 雙空白=4次
test1 = test.replace("  "," ",2) # 由左而右，替換 k 次'''



# https://pythonhow.com/start/cia
# Level 6
# 承上，從結尾開始的第270個單詞，和從頭開始的第270個單詞
questionNo += 1

#1 從左數來第270~271個空白之間那個詞，右邊同理
#2 或是，先把字串變成list，就可以利用 sort 後，很快找到
#3 strClean已先把.,移除掉了


# ============================================================
# 乾淨的純粹 Word list
# ============================================================
targetCleanList = targetClean.split(" ")

# 從結尾開始的第270個單詞
targetCleanList.reverse()  # 留意 reverse 是沒有 return值 的
ans6_1 = targetCleanList[269]

# 從頭開始的第270個單詞
targetCleanList.reverse()
ans6_2 = targetCleanList[269]

print("\n",questionNo,".","".join([ans6_1,ans6_2]))

# 如果你直接去 str 一個 list ， 而不是 "".join 他的話
# 會變成一個含有[]、逗點和空白的字串XD
test=["k1","k2","k3"]
strtest=str(test)       # strk= ['k1', 'k2', 'k3']，strk[0]= [
jointest="".join(test)  # joink= k1k2k3



# https://pythonhow.com/start/penatibuscondimentum
# Level 7
# 承上，使用每個單詞的最後一個字母創建一個字符串，並使用該字符串的最後三分之一
questionNo += 1
anstemp7 = []
ans7list = []

for j in range( len(targetCleanList) ):
    anstemp7.append( targetCleanList[j][ len(targetCleanList[j])-1 ] )

if len(anstemp7) % 3 == 0:
    ans7list = anstemp7[ int(len(anstemp7)*2/3)+1 : ]
    print("len(anstemp7)=",len(anstemp7),"，","len(ans7list)=",len(ans7list))
else:
    ans7list = anstemp7[ int(len(anstemp7)*2/3)+1 : ]
    print("len(anstemp7)=",len(anstemp7),"，","len(ans7list)=",len(ans7list))

# a = targetCleanList[0][ len(targetCleanList[0])-1 ]

print("\n",questionNo,".","".join(ans7list))



# https://pythonhow.com/start/tmecsasenmadauasossaldneicmtanaemcsmmts
# tmttttsussadmmtmsettxcsnssmmsttemmlssmnnostmtdreomeods
# Level 8
# 承上，包含大寫“q”的單詞
questionNo += 1

ans8list=[]
for i in range(len(targetCleanList)):
    if targetCleanList[i].count("Q") > 0 :     # target.find(" ") # 找位置
        ans8list.append(targetCleanList[i])
    else:
        pass

print("\n",questionNo,".","".join(ans8list))



# https://pythonhow.com/start/Quisque
# Level 9
# 承上，C + P的字母版本
# 長度4 且 後面有逗號的 單字總數C，長度4 且 後面有句號的 單字總數P
questionNo += 1


# ============================================================
# 不乾淨的 Word list
# ============================================================
targetList = target.split(" ")

countC=0
for i in range( len(targetList) ):
    if len( targetList[i] ) == 5 and targetList[i].count(",") >0:
        countC +=1
    else:
        pass

countP=0
for i in range( len(targetList) ):
    if len( targetList[i] ) == 5 and targetList[i].count(".") >0:
        countP +=1
    else:
        pass

print("C =",countC,"P =",countP)
ans9 = changeKeyword(countC + countP)


print("\n",questionNo,".",ans9)





# ============================================================
# 製作一個 Dict，其值為 index 的長度
# ============================================================

# 製作一個 Dict，以每個 word 為 index
def generateDictFromList(anyList):
    import string
    anyDict = dict.fromkeys(anyList, 0)    # 先都指派 0
    
    # 將每個index的長度指派給每一個index
    for i in anyList:
        anyDict[i] =  len(i)
    return dict(anyDict)                   # 必須要 dict 不然會是list

targetCleanDict = generateDictFromList(targetCleanList)
# print("targetCleanDict =",targetCleanDict)



'''當list[i]長度=4時，
從 list[i]這個字串位置開始，
去算 target(Str) 中 從此位置到最後 的逗號出現次數'''


C="A BB CCC, DDDD, EE. K, KK FFF, QQ CCCC, KK."
cleanC = strClean(C)
cleanCList = cleanC.split(" ")
# print("cleanCList =",cleanCList,"\n\n")

sumC = 0
copyC=C
copyCleanCList=cleanCList
for i in range( len(cleanCList) ):

    if len(cleanCList[i]) == 2:
        # print("i=",i)
        locationC = copyC.find(cleanCList[i])  # find，遇到重複字串會悲劇
        
        # tempC = C[ locationC :]
        # anstempD = tempC.count(",")
        anstempD = copyC.count(",",locationC,len(copyC))
        sumC += anstempD

        copyC = copyC[locationC+2 :]
        copyCleanCList = copyC.split(" ")
        # print("C =",C,"\ncopyC =",copyC,"\n")
        
        # print("locationC =",locationC,"anstempD =",anstempD,"ansD =",sumC)
        # print("\n\n")
        
    else :
        pass

'''# 字典可以通过以下方法调换 key和 value：
dic = { 'a': 1,
        'b': 2,
        'c': 3, }
reverse = {v: k for k, v in dic.items()}
# B.items() = dict_items([('A', 1), ('BB', 2), ('CCC', 3), ('DDDD', 4), ('E', 1)])

# 注意 2 點!
#1 原始 value 的类型,必须是不可变类型
#2 對於有重複value的dict，則會丟失訊息'''




# https://pythonhow.com/start/ca
# Level 10
# 承上，Number of days from Wednesday, November 24, 1892 to Jan, 1, 2000 In alphabetic form (0->a, 1->b, etc.)
# 1892年11月24日星期三至2000年1月1日的天數 以字母形式（0-> a，1-> b等）
questionNo += 1

import datetime
early = datetime.datetime(1892,11,24)
late = datetime.datetime(2000,1,1)
diff = late - early   # 39118 days, 0:00:00

# 留意 timedelta格式不是字串，且數字與days之間必夾一個空白
daysLocation = str(diff).find("days")
days = int(str(diff)[0: int(daysLocation) ]) # 39118

ans10 = changeKeyword(days)

print("\n",questionNo,".",ans10)



# https://pythonhow.com/start/djbbi
# Level 10 complepte !