
# 希望在不定義 function() 丟入的變數是啥的情況下
# 計算 function() 的運行時間
def time(function):
    import time
    t1 = time.time()
    function()
    t2 = time.time()
    print("耗費時間 = {:>9.16f}\n".format(t2-t1) )

def add1(x):
    print("跑 x+1 扔回答案")
    return x+1


# 丟進去的是函式，但這樣不行，
# 要先讓丟進去的東西，假裝他也是一個變數，讓time去吃
time( lambda : add1(1) )






def beTest1():
    print("print出 test1")

def beTest2(a):
    print("print出 a =" ,a)

# 丟進去的是函式，但這樣不行，
# 要先讓丟進去的東西，假裝他也是一個變數，讓time去吃
time(lambda : beTest1())
time(lambda : beTest2(123))


