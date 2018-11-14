'''
幫 array 加一個 any 的 function，可以輸入任一 function，
如果任何一個元素丟進那 function 裡面的值是 true，就輸出 true，
否則就 false。

例如說現在有個 function 叫做：isGreaterThanZero，範例就會是這樣：

[1, 2, 3, 4, 5].any(isGreaterThanZero); //=> true
[-1, 0].any(isGreaterThanZero); //=> false

'''


def isGreaterThanZero(list):
    ans = bool
    list.sort()

    if len(list) != 0 and list[0] >= 0:
        ans = True
    else :
        ans = False
    
    return ans


def any(function):
    ans = bool
    if function():
        ans = True
    else:
        ans = False
    return ans


# 希望在不定義 function() 丟入的變數是啥的情況下
# 計算 function() 的運行時間
def time(function):
    import time
    t1 = time.time()
    function()
    t2 = time.time()
    print("耗費時間 = {:>9.16f}".format(t2-t1) )




list = [1006, 432121352, 345453.45, 45452121, -1 ,545 ,145 ,574874]

print( isGreaterThanZero(list) )

print( any( lambda : isGreaterThanZero(list) ) )


# 丟進去的是函式，但這樣不行，
# 要先讓丟進去的東西，假裝他也是一個變數，讓time去吃
time( lambda : isGreaterThanZero(list) )
