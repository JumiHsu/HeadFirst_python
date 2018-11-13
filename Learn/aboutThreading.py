import threading
import time

# ==============================================
# 建立子執行緒
# ==============================================

# 子執行緒的工作函數
def job():
  for i in range(5):
    print("Child thread:", i)
    time.sleep(1)

# 建立一個子執行緒
t = threading.Thread(target = job)
# 執行該子執行緒
t.start()


# 主執行緒繼續執行自己的工作
for i in range(3):
  print("Main thread:", i)
  time.sleep(1)


# 等待 t 這個子執行緒結束
t.join()               # 沒有這一句，Done就會在 主執行緒結束後 就立即出現

print("Done.\n")





# ==============================================
# 多個子執行緒與參數
# ==============================================

# 子執行緒的工作函數
def jobNum(num):
  print("Thread", num)
  time.sleep(1)

# 建立 5 個子執行緒
threads = []
for i in range(5):
  threads.append(threading.Thread(target = jobNum, args = (i,)))
  threads[i].start()

# 主執行緒繼續執行自己的工作
# ...

# 等待所有子執行緒結束
for i in range(5):
  threads[i].join()

print("Done.")





# ==============================================
# TRY
# ==============================================
'''
# import thread
import time
import random

count = 0
def threadTest():
    global count
    for i in range(10000):
        count += 1
for i in range(10):
    threads.start_new_thread(threadTest, ())	#如果对start_new_thread函数不是很了解，不要着急，马上就会讲解
time.sleep(3)
print(count)	#count是多少呢？是10000 * 10 吗？
'''