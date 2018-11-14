
# 第一題：寫一個 reverse 的 function，反轉字串


# 思路：字串轉list，然後再sort(,inverse=True)

# 先整理字串
def clean(anystr):
    print("原始字串anystr =" ,anystr)
    anystr.strip() # 整理字串頭尾、去掉換行 & 空白
    print("整理後anystr =" ,anystr)
    return anystr


# 如果為連續字串
strContinue_Tw = "生日快樂"
strContinue_En = "HappyBirthday"

def ReverseContinue(anystr):
    anylist = list(anystr)
    print("轉list後 =" ,anylist)
    anylist.reverse()
    print("Reverse後 =" ,anylist)
    return anylist


# 如果為有符號分隔之字串
strDiscrete_space = "Happy birthday to you"
strDiscrete_point = "www.google.com.tw"

def ReverseDiscreteSpace(anystr):
    anylist = anystr.split()
    print("清除空白，轉list後 =" ,anylist)
    anylist.reverse()
    print("Reverse後 =" ,anylist)
    return anylist

def ReverseDiscretePoint(anystr):
    anylist = anystr.split(".")
    print("清除點號，轉list後 =" ,anylist)
    anylist.reverse()
    print("Reverse後 =" ,anylist)
    return anylist


# a = clean(strContinue_En)
ReverseContinue( strContinue_Tw )
ReverseContinue( strDiscrete_point )
ReverseDiscretePoint( strDiscrete_point )
ReverseDiscreteSpace( strDiscrete_space )


# ReverseContinue( lambda:clean(strContinue_En) )

# print( ReverseContinue( lambda:clean(strContinue_En) ) )
# print( ReverseContinue( lambda:clean(strContinue_Tw) ) )

print(  )
print(  )
print(  )













# 整理句子中的髒東西
strDiscrete_sentance = " Happy  birthday to you.   \n"

'''
print( strDiscrete_sentance )
print( strDiscrete_sentance.strip() )
print( strDiscrete_sentance.lstrip() )
print( strDiscrete_sentance.rstrip() )

'''




'''
def strReverse(anystr):
    point = "."
    space = " "
    anylist = []
    print("anystr =" ,anystr)
    anystr.strip() # 整理字串頭尾、去掉換行 & 空白
    print("整理後anystr =" ,anystr)

    if  space in anystr and anystr.count(point) > 0 :
        anystr.replace(".","")
        anylist = anystr.split(space)
        print("split(space)後 =" ,anylist)
        
    elif space in anystr  or  point in anystr:
        anylist = anystr.split(space)
        anylist = anystr.split(point)
        print("split(space)後 =" ,anylist)
    else:
        anylist = list(anystr)
        print("轉list後 =" ,anylist)
    
    return anylist ,anylist.reverse()



print( "Reverse前後的" ,"strContinue_Tw =" ,strReverse(strContinue_Tw) ,"\n")
print( "Reverse前後的" ,"strContinue_En =" ,strReverse(strContinue_En) ,"\n")

print( "Reverse前後的" ,"strDiscrete_space =" ,strReverse(strDiscrete_space) ,"\n")
print( "Reverse前後的" ,"strDiscrete_point =" ,strReverse(strDiscrete_point) ,"\n")

print( "Reverse前後的" ,"strDiscrete_sentance =" ,strReverse(strDiscrete_sentance) ,"\n")

'''