# -*- coding: utf-8 -*-

import time
from threading import Thread

class worker(Thread):
    def run(self):
        print("工作開始\n")
        t1 = time.time()
        for x in range(0,11):
            # print x
            time.sleep(1)
        t2 = time.time()
        print("工作結束，共耗時 = {:>9.16f}".format(t2-t1))

def timeSpent(function):
    import time
    print("計時開始")
    t1 = time.time()
    function()
    t2 = time.time()
    print("計時結束，共耗時 = {:>9.16f}".format(t2-t1))

def run():
    worker().start()

timeSpent(lambda: run())