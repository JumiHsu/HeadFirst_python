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


# ==============================================
# 建立子執行緒
# ==============================================
import threading

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





print("\n========== 練習 ==========")
# 創建一個 Animal 的類別，必須包含：物種名稱、重量
# 以及 一個 Animal類型的物件，他可以進行吃的動作
class Animal():
    def __init__(self, inputName ,inputKg): # 定義 這個class，包含哪些必須設定的屬性參數
        self.name = inputName     # 定義 以後要怎麼呼叫
        self.kg = inputKg

    def eat(self ,nameFood ,kgFood):
        if kgFood <= 0:
            kgFood = 0
            print("食物重量需大於 0")
        else:
            pass
        self.nameFood = nameFood
        self.kgFood = kgFood
        self.kg += kgFood

    def shit(self ,kgShit):
        if kgShit <= 0:
            kgShit = 0
            print("排泄物重量需大於 0")
        else:
            pass
        self.kgShit = kgShit
        self.kg -= kgShit


animalEx1 = Animal("小黑",52)      # 建立一個實體物件，名叫dog，具備 Animal特徵
print("animalEx1的體重 =" ,animalEx1.kg)           # 調用該物件的特定屬性，方式 1


animalEx1.eat("apple",2)     # 進行該類別下的def動作，改變該類別物件的屬性參數
print( animalEx1.name ,"吃飯了! 體重變為 =" ,animalEx1.kg)

animalEx1.shit(3)
print( animalEx1.name ,"拉*了! 體重變為 =" ,animalEx1.kg)


