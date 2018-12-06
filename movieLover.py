
from __future__ import unicode_literals
import json

def changeJson(anyDict):
    # 使用 unicode_literals + ensure_ascii=False 處理 import json 亂碼的問題
    anyDictJson = json.dumps(anyDict ,indent=4 ,ensure_ascii=False)
    print("=",anyDictJson)
    return anyDictJson




for i in ["a","b","c"]:
    locals()["abc%s"%i + "de"] = 2
    locals()["Element_%s"%i + "_is_"] = 3





nameList = ["Jumi","Kao","BananaNana","Fionana","さくら","小狼"]

# 刪除
nameList.remove("Fionana")  # 如果remove的東西不存在，會卡住哦
print(nameList)

# 在指定位置，增加element
nameList.insert(3,"Fionana")
print(nameList)


# 填入每個人的戰鬥力

# 【方法1】先製作一個 Dict 先都填入0，但我還不會逐個填入值
nameDict01 = dict.fromkeys(nameList,0)
nameDict01Json = changeJson(nameDict01)


# 【方法2】先製作戰鬥力 List，再把兩個 list zip 後，轉 dict
atk = [84,1111,9999,666,520,520]
nameDict02 = dict( zip(nameList,atk) )
nameDict02Json = changeJson(nameDict02)

'''
# 如果現在新增第2個變數
defence = [20,30,40,50,60,70]
nameDict03 = dict( zip(nameList ,atk ,defence) )

nameDict03Json = json.dumps(nameDict03 ,indent=4 ,ensure_ascii=False)
print(nameDict03Json)
'''

