

''' 功能：print 出一個，混和 str/int/list 形式的
    巢狀 list，並在 內嵌list 前縮排。
    return：無'''

import sys

# 綜合版本
def print_nest_indent(list, opt="marson", indent=0 ,level=0 ,fn=sys.stdout):
    if opt == "marson":
        print_nest_indent_marson(list ,indent=4)
    elif opt == "marson_ori":
        print_nest_indent_marson_rec(list, indent=4, level=0 )

    elif opt == "book":
        print_nest_level(list,level=0)           # level = 統一縮排TAB數
    elif opt == "txt":
        nestPrintTxt(list,level=0,fn=sys.stdout)

    elif opt == "jumi":
        print_nest_indent_jumi(list, indent=4)

    else:
        print(msg02)

msg01 = "plz check，具有不為 str、int、list 的 element"
msg02 = "plz check，參數錯誤"





# 馬森
# 功能差異：可在 內嵌list 前縮排。（此為完整參數版本）
def print_nest_indent_marson_rec(items, indent, level, space=" "):
    for item in items:
        if isinstance(item, str) or isinstance(item, int):
            print((space * indent * level) + str(item))

        elif isinstance(item, list):
            print_nest_indent_marson_rec(item, level + 1, indent, space)

        else:
            print(msg01)

# indent =每次縮排空白數
def print_nest_indent_marson(items, indent=4):
    print_nest_indent_marson_rec(items, 0, indent, " ")




# 深入淺出
# 功能新增：每列左方，皆可統一縮排 level 個TAB
def print_nest_level(anyList, level=0):
    
    for eachItem in anyList:
        if isinstance(eachItem,list):
            print_nest_level(eachItem, level+1)  # 內嵌的list，左邊縮排量=level+1

        elif isinstance(str(eachItem), str) or isinstance(int(eachItem), int):
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

            elif isinstance(str(eachItem), str) or isinstance(int(eachItem), int):
                print(space*indent*count + str(eachItem))

            else:
                print(msg01)

    identifyIndent_nestPrint(anyList, count, indent, space)




# 深入淺出 2
# 功能新增：可設定要寫入哪個檔案
def nestPrintTxt(anyList, level=0, fn=sys.stdout):
    for eachItem in anyList:
        if isinstance(eachItem,list):
            nestPrintTxt(eachItem, level+1 ,fn)  # 內嵌的list，左邊縮排量=level+1

        elif isinstance(str(eachItem), str) or isinstance(int(eachItem), int):
            for tab_stop in range(level):
                print("\t",end="" ,file=fn)
            print(eachItem, file=fn)        # 用 print 來寫入文件 (why?)

        else:
            print(msg01)


# 函數名稱不可與檔名相同
# 註解 50字 長度最佳

