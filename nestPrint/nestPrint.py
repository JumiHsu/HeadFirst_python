

''' 函數名稱： print_nest_indent
    參數：anyList, indent(縮排，預設值=4)
    功能：print 出一個，混和 str、int、list 形式的
    　　　巢狀 list，並在遇到 內嵌list 時縮排
    return：無'''

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
                print("plz check，具有不為 str、int、list 的element，或者 indent 出現負數。")                
    identifyIndent_nestPrint(anyList, count, indent, space)
print("\n----- nestPrint.print_nest_indent(anyList, indent) 匯入成功 -----")




''' 函數名稱： print_nest_level(anyList, level)
    參數：一組 list，level縮排數量(預設值=0)
    功能：print 出一個，混和 str、int、list 形式的
    　　　巢狀 list，每一列左方統一縮排(以level為單位)。
    return：無'''

def print_nest_level(anyList, level=0):
    
    for eachItem in anyList:
        if isinstance(eachItem,list):
            print_nest_level(eachItem, level+1)  # 內嵌的list，左邊縮排量=level+1

        elif isinstance(eachItem, str) or isinstance(eachItem, int):
            for tab_stop in range(level):
                print("\t",end="")               # 最上層的list，左邊縮排量=level
            print(eachItem)

        else:
            print("plz check，具有不為 str、int、list 的element，或者 level 出現負數。")
print("\n----- nestPrint.print_nest_level(anyList, level) 匯入成功 -----")


# 函數名稱不可與檔名相同
# 註解 50字 長度最佳
