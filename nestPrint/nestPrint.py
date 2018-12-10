

''' 模組名稱：identifyType_nestPrint(anyList)
    參數：一組 list
    功能：print 出一個，混和 str、int、list 形式的，巢狀 list
    return：無'''

print("\n----- nestPrint.identifyType_nestPrint(anyList) 匯入成功 -----")
def identifyType_nestPrint(anyList):
    for i in anyList:
        if isinstance(i,str) or isinstance(i,int):
            print(i)
        elif isinstance(i,list):
            identifyType_nestPrint(i)
        else:
            print("plz check，具有不為 str、int、list 的element")

