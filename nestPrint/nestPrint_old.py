

''' 功能：print 出一個，混和 str/int/list 形式的
    巢狀 list，並在 內嵌list 前縮排。
    return：無'''
def a(list):
    print_nest_indent(list,4)


# 功能差異：可在 內嵌list 前縮排。（建議使用此版本）
def print_nest_indent_marson(items, indent=4):
    print_nest_indent_rec(items, 0, indent, " ")


# 功能差異：可在 內嵌list 前縮排。
def print_nest_indent(anyList, indent=4 ):
    count = 0
    space = " "

    def identifyIndent_nestPrint(anyList,count,indent,space):
        for eachItem in anyList:
            if isinstance(eachItem, list):
                # count += 1
                identifyIndent_nestPrint(eachItem, count+1, indent, space)
            
            elif isinstance(eachItem,str) or isinstance(eachItem,int):
                print(space*indent*count + str(eachItem))

            else:
                print("plz check，具有不為 str、int、list 的element")
    identifyIndent_nestPrint(anyList, count, indent, space)
print("\n----- print_nest_indent() 匯入成功 -----")




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
            print("plz check，具有不為 str、int、list 的element")
print("\n----- print_nest_level() 匯入成功 -----")





# 馬森版本
# 功能差異：可在 內嵌list 前縮排。（此為完整參數版本）
def print_nest_indent_rec(items, level, indent, space):
    for item in items:
        if isinstance(item, str) or isinstance(item, int):
            print((space * indent * level) + str(item))

        elif isinstance(item, list):
            print_nest_indent_rec(item, level + 1, indent, space)

        else:
            print("plz check，具有不為 str、int、list 的 element")

# 功能差異：可在 內嵌list 前縮排。（建議使用此版本）
def print_nest_indent_marson(items, indent = 4):
    print_nest_indent_rec(items, 0, indent, " ")

print("\n----- print_nest_indent_marson() 匯入成功 -----")

# 函數名稱不可與檔名相同
# 註解 50字 長度最佳
