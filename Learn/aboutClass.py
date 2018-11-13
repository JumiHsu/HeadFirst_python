# import time
# from threading import Thread



print("\n========== 創建一個class ==========")
# https://reurl.cc/Nrl7Q
# 看不懂 vscode 給的定義
    # def __init__(self, *args, **kwargs):
    #     return super().__init__(*args, **kwargs)


# 創建一個 Animal 的類別，必須包含：物種名稱、重量
# 以及 一個 Animal類型的物件，他可以進行吃的動作
class Animal():
    def __init__(self, inputName ,inputKg): # 定義 這個class，包含哪些必須設定的屬性參數
        self.name = inputName               # 定義 以後要怎麼呼叫
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

def whatName(self):                                # 調用該物件的特定屬性，方式 2
    return animalEx1.name
print("animalEx1的名字 =" ,whatName(animalEx1) )


animalEx1.eat("apple",2)     # 進行該類別下的def動作，改變該類別物件的屬性參數
print( animalEx1.name ,"吃飯了! 體重變為 =" ,animalEx1.kg)

animalEx1.shit(3)
print( animalEx1.name ,"拉*了! 體重變為 =" ,animalEx1.kg)






print("\n========== 存提款 ==========")
class Account():
    def __init__(self ,accountID ,accountPassword):
        self.ID = accountID
        self.Password = accountPassword
        self.balance = 0                           # 結餘 = 0 ?


    def deposit(self ,amount):
        if amount <= 0:
            raise ValueError('存款額度必須 > 0')        # 這一句會報錯，還不懂為什麼
        else :
            pass
        self.Deposit = amount
        self.balance += amount


    def withdrow(self ,amount):
        if amount <= 0:
            raise ValueError('提款額度必須 > 0')        # 同理
        elif amount > self.balance:
            # raise ValueError('餘額不足')
            raise RuntimeError('balance not enough')   # 這一句會報錯，還不懂為什麼
        else :
            pass
        self.Withdrow = amount
        self.balance -= amount


# 創建一個 帳戶Jumi
accountJumi = Account("Jumi" ,20181113)
print("帳戶ID =" ,accountJumi.ID ,"\n帳戶密碼 =" ,accountJumi.Password ,"\n帳戶餘額 =" ,accountJumi.balance)


# 對 帳戶Jumi 這個具備帳戶特性的物件，進行：
# 存款
accountJumi.deposit(1000)             # 可 try 0元
print("存款後，帳戶餘額 =" ,accountJumi.balance)

# 提款
accountJumi.withdrow(200)             # 可 try 2000元
print("提款後，帳戶餘額 =" ,accountJumi.balance)


# print("提款後，帳戶餘額 =" ,accountJumi.withdrow(200).balance())  # 這樣會報錯，不知道為什麼





'''
# 幾個看不懂，而且會報錯的：

# 1.可以使用default
class AnimalWeb():
    def __init__(self, name):
        self.name = name
a = AnimalWeb("dog")
print(a.name)


# 延續簡單範例1，此時如果呼叫 b=AnimalWeb() 
# 就會出錯，因為你沒有給他name的屬性
b = AnimalWeb()
print(b.name)


# 可以先給一個預設值，這樣第一次呼叫就不用給屬性
# 如果是固定的值，呼叫時也不用給了，直接設定就好
class AnimalWeb():
    def __init__(self, name = default):
        self.name = name

a = AnimalWeb('動物')
print(a.name)


# 當然，也是可以是空的，之後再新增資料就好
class AnimalWeb():
    def __init__(self):
        self.data = []
a = AnimalWeb()
a.data.append(123456)





# 2: __init__並不是必要的

# 簡單來說，python class自由度很高

# 你也可以這樣，直接給屬性，不透過__init__
class AnimalWeb():
    name="dog" #把參數寫在init外面
    def __init__(self):
        pass
a = AnimalWeb()
print(a.name)


# 需要屬性時，我不見得一定要在init裡設定
# 也不見得一定要在class裡設定，就像下面這樣
class AnimalWeb():
    def __init__(self):
        pass
a = AnimalWeb()
a.name="dog"  #自己給屬性與參數
print(a.name)
# 可以在使用 AnimalWeb 這個類別之後，再自己新增屬性

'''


print("---------------- 練習 END -------------------")
