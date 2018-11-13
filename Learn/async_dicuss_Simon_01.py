import time
from threading import Thread

class worker(Thread):
    def run(self):
        for x in range(0,11):  # for x in xrange(0,11):
            print(x)
            time.sleep(1)

class waiter(Thread):
    def run(self):
        for x in range(100,103): # for x in xrange(100,103):
            print(x)
            time.sleep(5)


def timeSpent(function):
    import time
    t1 = time.time()
    function()
    t2 = time.time()
    print("Time spent = {:>9.16f}".format(t2-t1))


def run():
    worker().start()
    waiter().start()


# 計算 run() 這個函數要跑多久時間
timeSpent(lambda: run())

