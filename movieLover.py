
from __future__ import unicode_literals
import json

print("=========================== START ===========================")

# ========================================================================
# 轉Json
# ========================================================================
def changeJson(anyDict):
    # 使用 unicode_literals + ensure_ascii=False 處理 import json 亂碼的問題
    anyDictJson = json.dumps(anyDict ,indent=4 ,ensure_ascii=False)

    # 取得 變數名稱 作為 字串
    variable_name = [
    k for k,v in locals().items()
    if v is anyDict ][0]

    print("\n[changeJson]把變數名稱印出來 =",variable_name)
    a='{name} is {age} years old!'.format(name = 'Justin', age = 35)
    print(a)
    # print( "\nValue1 : %s" %  anyDictJson  )
    # print( "\nValue2 : %s" %  locals()  )
    # print( "\nValue3 :" , anyDictJson)

    # print("\nanyDictJson =",anyDictJson)
    # print("\nlocals()=",locals())
    # print("\nlocals().keys =",locals().keys)
    return anyDictJson





# ========================================================================
# 嘗試撰寫中
# ========================================================================
def printName(anyDict):
    # 取得 變數名稱 作為 字串
    variable_name = [
    k for k,v in locals().items()
    if v is anyDict ][0]

    print("\n[printName]把變數名稱印出來 =",variable_name)
    return anyDict



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
nameDict01Json = changeJson(nameDict01)

# for i in [0,1,2,3,4,5]:
#     for j in range(5):
#         nameDict01 = dict.fromkeys(nameList[j],i)
#         print(nameDict01)



# 【方法2】先製作戰鬥力 List，再把兩個 list zip 後，轉 dict
atk = [84 ,1111 ,9999 ,666 ,520 ,520]
nameDict02 = dict( zip(nameList,atk) )
nameDict02Json = changeJson(nameDict02)




# 如果現在新增第2個變數
defence = [20,30,40,50,60,70]
data=[]
for x,y in zip(atk,defence):
    data.append((x,y))

nameDict03 = dict( zip(nameList ,data) )
nameDict03Json = json.dumps(nameDict03 ,indent=4 ,ensure_ascii=False)


for each in atk:
    print("index",atk.index(each),"=",each)



print("\n=========================== FINISH ===========================")