

''' 
函數名稱： time
參數：lambda : func()
功能：對任意 function() ，計算運行時間
使用方式：time( lambda : func() )
return：無'''

def time(function = lambda : desc()):
    import time
    t1 = time.time()
    function()
    t2 = time.time()
    print("耗費時間 = {:>9.16f}\n".format(t2-t1) )

def desc():
    print("請丟進 lambda : func()，以計算 func 的運行時間")

# 丟進去的是函式，但這樣不行，
# 要先讓丟進去的東西，假裝他也是一個變數，讓time去吃

