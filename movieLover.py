
from __future__ import unicode_literals
import json

print("=========================== START ===========================")

# ========================================================================
# 轉Json（1個key → 1個value）
# ========================================================================
def changeJson(anyDict ,anyDictName="anyDictJsonName"):
    # 使用 unicode_literals + ensure_ascii=False 處理 import json 亂碼的問題
    anyDictJson = json.dumps(anyDict ,indent=2 ,ensure_ascii=False,separators=(",",":"))
    print(anyDictName,"(一)=",anyDictJson)

    return anyDictJson     # return 的會是一個 str



# ========================================================================
# 轉Json（1個key → 1個tuple value）
# ========================================================================
def changeJsonTuple(anyDict ,anyDictName="anyDictJsonName"):
    # 使用 unicode_literals + ensure_ascii=False 處理 import json 亂碼的問題
    anyDictJson = json.dumps(anyDict ,indent=1 ,ensure_ascii=False,separators=(",",":"))
    # print(anyDictName,"(一)=",anyDictJson)
    
    temp= anyDictJson.replace(",\n",",")
    temp= temp.replace("],","],\n")
    print(anyDictName ,"(二)=",temp,"\n")

    return anyDictJson     # return 的會是一個 str







# ========================================================================
# 嘗試撰寫中 1
# ========================================================================
def printName(anyDict):
    # 取得 變數名稱 作為 字串
    variable_name = [
    k for k,v in locals().items()
    if v is anyDict ][0]

    print("\n[printName]把變數名稱印出來 =",variable_name)
    return anyDict
    # print( "\nValue1 : %s" %  anyDictJson  )
    # print( "\nValue2 : %s" %  locals()  )
    # print( "\nValue3 :" , anyDictJson)

    # print("\nanyDictJson =",anyDictJson)
    # print("\nlocals()=",locals())
    # print("\nlocals().keys =",locals().keys)



# ========================================================================
# 嘗試撰寫中 2
# ========================================================================
dict01 = {'Name': 'Zara', 'Age': 7}
print( "Value : %s" %  dict01.keys()  )
# Value : dict_keys(['Name', 'Age'])

printName(dict01)
# [printName]把變數名稱印出來 = anyDict





# ========================================================================
# 依序 print 出 List 中的值
# ========================================================================
def printList(List):
    print("\n")
    for each in List:
        print("List[",List.index(each) ,"] =" ,each)
        # 找位置：字串用find，列表用index




# ========================================================================
# 嘗試有邏輯的產生變數名稱
# ========================================================================
nameTest=[]
for i in ["a","b","c"]:
    locals()["abc%s"%i + "de"] = 2          # 有規律的產生變數名稱，並且令值為2
    locals()["Element_%s"%i + "_is_"] = 3
    nameTest.append("abc%s"%i + "de")

# printList(nameTest)






# ========================================================================
# 正文開始
# ========================================================================
nameList = ["Jumi","Kao","BananaNana","Fionana","さくら","小狼"]
printList(nameList)



# 刪除 & 增加
nameList.remove("Fionana")     # 如果remove的東西不存在，會卡住哦
nameList.insert(3,"Fionana")   # 在指定位置，增加element


# 填入每個人的戰鬥力

# 【方法1】先製作一個 Dict 先都填入0，但我還不會逐個填入值
nameDict01 = dict.fromkeys(nameList,0)
nameDict01Json = changeJson(nameDict01 ,"nameDict01Json")


# 【方法2】先製作戰鬥力 List，再把兩個 list zip 後，轉 dict
atk = [84 ,1111 ,9999 ,666 ,520 ,520]
nameDict02 = dict( zip(nameList,atk) )
nameDict02Json = changeJson(nameDict02 ,"nameDict02Json")



# 如果現在新增第2個變數，需要先把 data變數先 zip，再讓 data 與 key 去 zip
defence = [20,30,40,50,60,70]
data=[]
for x,y in zip(atk,defence):
    data.append((x,y))

nameDict03 = dict( zip(nameList ,data) )
nameDict03Json = changeJsonTuple(nameDict03 ,"nameDict03Json")


for each in atk:
    print("index",atk.index(each),"=",each)
print("\n")



# 如果是一個，表中表中表的話呢?
movie = ["片名：La la Land",2016,"導演：Damien Chazelle",
        ["主演1：Sebastian Wilder","主演2：Mia Dolan","主演3：Keith",
        ["音樂：Justin Hurwitz","編劇：Damien Chazelle"]]]

print("編劇 =",movie[3][3][1])

for i in movie:
    print(i)



print("\n------------ 方法一：if type(x) is -------------")
# 如果你想要把最內層的列表資料也print出來的話?
# 方法 1（還沒看書之前）：if type(x) is list  return  Boolin
for i in movie:
    if type(i) is str or type(i) is int:
        print(i)
    elif type(i) is list:
        for j in i:
            if type(j) is str or type(j) is int:
                print(j)
            else:
                for k in j:
                    print(k)
    else:
        print("plz check")



print("\n------------ 方法二：isinstance -------------")
# 方法 2（書上教的）：isinstance(x,list)  return Boolin
for i in movie:
    if isinstance(i,str) or isinstance(i,int):
        print(i)
    elif  isinstance(i,list):
        for j in i:
            if isinstance(j,str) or isinstance(j,int):
                print(j)
            else:
                for k in j:
                    print(k)
    else:
        print("plz check")



print("\n------------ 方法一(不懂的bug)：if type(x) is -------------")
for i in movie:
    if type(i) is str or int:       #1 如果這邊條件改這樣
        print(i)
    elif type(i) is list:           #1 會讓 list 無法逐個 print
        for j in i:
            if type(j) is str or int :  #2 如果這邊改這樣
                print(j)
            else:                       #2 影響的就是這裡
                for k in j:
                    print(k)
    else:
        print("plz check")


# BIF：不是70幾個嗎?
# print("\n",dir(__builtins__),"數量=",len(dir(__builtins__)))
# help(input)



print("\n------------ NEXT：遞迴，使用 def -------------")
def identifyType_Print(anyList):
    for i in anyList:
        if isinstance(i,str) or isinstance(i,int):
            print(i)
        elif isinstance(i,list):
            identifyType_Print(i)
        else:
            print("plz check，具有不為 str、int、list 的element")

identifyType_Print(movie)


# 接下來是發布模組並安裝
# 開啟cmd，在setup.py的當前路徑下，輸入：
#1 setup.py sdist
#2 setup.py install


print("\n------------ NEXT：加上更多參數 -------------")
for i in movie:
    space=" "
    indent=2
    if isinstance(i, str) or isinstance(i, int):
        print(i)
    elif isinstance(i, list):
        for j in i:
            if isinstance(j, str) or isinstance(j, int):
                print(space*indent + j)
            else:
                for k in j:
                    print(space*indent*2 + k)
    else:
        print("plz check")



print("\n------------ NEXT：加上更多參數 2 -------------")
count=0
for i in movie:
    space = " "
    indent = 2
    if isinstance(i, str) or isinstance(i, int):
        print(count*indent*space + str(i))
    elif isinstance(i, list):
        count += 1
        for j in i:
            if isinstance(j, str) or isinstance(j, int):
                print(space*indent*count + str(j))
            else:
                count += 1
                for k in j:
                    print(space*indent*count + str(k) )
    else:
        print("plz check")




print("\n------------ NEXT：加上更多參數後，嘗試遞迴他 -------------")
count = 0
space = " "
indent = 2
for i in movie:
    if isinstance(i, str) or isinstance(i, int):
        print(count*indent*space + str(i))
    elif isinstance(i, list):
        count += 1
        for j in i:
            if isinstance(j, str) or isinstance(j, int):
                print(space*indent*count + str(j))
            else:
                count += 1
                for k in j:
                    print(space*indent*count + str(k))
    else:
        print("plz check")



def identifyType_Print_indent(anyList ,indent=2):
    count = 0
    space = " "
    def nestPrint_indent(anyList, count, indent, space):
        for i in anyList:
            if isinstance(i, str) or isinstance(i, int):
                print(space*indent*count + str(i))

            elif isinstance(i, list):
                count += 1
                nestPrint_indent(i, count, indent, space)

            else:
                print("plz check，具有不為 str、int、list 的element")

    nestPrint_indent(anyList, count, indent, space)



print("\n撰寫中，測試結果：")
identifyType_Print_indent(movie,2)





print("\n=========================== FINISH ===========================")
