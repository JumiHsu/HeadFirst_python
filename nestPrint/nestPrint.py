

''' 功能：print 出一個，混和 str/int/list 形式的
    巢狀 list，並在 內嵌list 前縮排。
    return：無'''

# 綜合版本
def print_nest_indent(list, opt=0, indent=0 ,level=0 ,sysbol=" "):
    if opt == 0:
        print_nest_indent_marson(list ,indent=4) # indent =每次縮排空白數
    elif opt == 1:
        print_nest_level(list,level=0)           # level = 統一縮排TAB數
    elif opt == 2:
        print_nest_indent_jumi(list, indent=4)
    elif opt == "ori":
        print_nest_indent_marson_rec(list, indent=4, level=0, space=sysbol )
    else:
        print(msg02)

msg01 = "plz check，具有不為 str、int、list 的 element"
msg02 = "plz check，參數錯誤"





# 馬森
# 功能差異：可在 內嵌list 前縮排。（此為完整參數版本）
def print_nest_indent_marson_rec(items, indent, level, space):
    for item in items:
        if isinstance(item, str) or isinstance(item, int):
            print((space * indent * level) + str(item))

        elif isinstance(item, list):
            print_nest_indent_marson_rec(item, level + 1, indent, space)

        else:
            print(msg01)

# 功能差異：可在 內嵌list 前縮排。（建議使用此版本）
def print_nest_indent_marson(items, indent=4):
    print_nest_indent_marson_rec(items, 0, indent, " ")




# 深入淺出
# 功能差異：除了遇到 內嵌list 時縮排，且每列左方，皆可統一縮排 level 個TAB
def print_nest_level(anyList, level=0):
    
    for eachItem in anyList:
        if isinstance(eachItem,list):
            print_nest_level(eachItem, level+1)  # 內嵌的list，左邊縮排量=level+1

        elif isinstance(eachItem, str) or isinstance(eachItem, int):
            for tab_stop in range(level):
                print("\t",end="")               # 最上層的list，左邊縮排量=level
            print(eachItem)

        else:
            print(msg01)




# Jumi練習
# 功能差異：可在 內嵌list 前縮排。
def print_nest_indent_jumi(anyList, indent=4):
    count = 0
    space = " "

    def identifyIndent_nestPrint(anyList, count, indent, space):
        for eachItem in anyList:
            if isinstance(eachItem, list):
                # count += 1
                identifyIndent_nestPrint(eachItem, count+1, indent, space)

            elif isinstance(eachItem, str) or isinstance(eachItem, int):
                print(space*indent*count + str(eachItem))

            else:
                print(msg01)
    identifyIndent_nestPrint(anyList, count, indent, space)


# 函數名稱不可與檔名相同
# 註解 50字 長度最佳

