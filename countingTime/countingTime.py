

''' 函數名稱： time
    參數：function
    功能：在不定義 function() 丟入的變數是啥的情況下計算 function() 的運行時間
    使用方式：time( lambda : test() )
    return：無'''

def time(function):
    import time
    t1 = time.time()
    function()
    t2 = time.time()
    print("耗費時間 = {:>9.16f}\n".format(t2-t1) )

print("\n----- countingTime.time( function ) 匯入成功 -----")

# 丟進去的是函式，但這樣不行，
# 要先讓丟進去的東西，假裝他也是一個變數，讓time去吃
'''
def test():
    print("TEST")
time( lambda : test() )
'''

