import json
from pprint import pprint

# 定義一張撲克牌
class pokerCard():
        s = "spade"
        h = "heart"
        d = "dimond"
        c = "club"
        def __init__(self, suit, figure):
            self.suit = suit
            self.figure = figure


# 定義一手 5 張撲克牌
class inHand():
    def __init__(self,handCard01,handCard02,handCard03,handCard04,handCard05):
        self.handCard01 = handCard01
        self.handCard02 = handCard02
        self.handCard03 = handCard03
        self.handCard04 = handCard04
        self.handCard05 = handCard05

    # # 定義幾種牌型，依照優先序
    # def fourOfaKind():
    #     if inHand[i]

card1 = pokerCard(pokerCard.s,12)

# 生成一副牌，存成字典，排上流水號1~53
aDeck = dict.fromkeys(range(1,54), 0)

aDeckJson = json.dumps(aDeck,indent=4)
print("aDeck前 =",aDeckJson)

fourSuit = [pokerCard.s,pokerCard.h,pokerCard.d,pokerCard.c]
allFigure = range(1,14)





# i,j,k=0,0,1
# for k in aDeck:
#     if i < len(fourSuit) and j < len(allFigure):
#         aDeck[k] = ( fourSuit[i] , allFigure[j] )
#         j += 1
    
#     elif i < len(fourSuit) and j == len(allFigure):
#         j = 0
#         i += 1
#         aDeck[k] = ( fourSuit[i] , allFigure[j] )

#     elif i == len(fourSuit) and j == len(allFigure):
#         print("i == len(fourSuit) and j == len(allFigure) 導致 break")
#         break
    
#     elif k == len(aDeck):
#         print("k == len(aDeck) 導致 break")
#         break
#     else :
#         print("else，check")



    #     if j < len(allFigure) :
    # # Deck.append(pokerCard(i,j))
    # aDeck[k] = ( fourSuit[i] , allFigure[j] )
    # i += 1
    # j += 1
    # k += 1



fourSuit = [pokerCard.s,pokerCard.h,pokerCard.d,pokerCard.c]
allFigure = range(1,14)

k=0
while k < 52:
    for i in ["s","h","d","c"] :
        for j in range(0,14) :
            # Deck.append(pokerCard(i,j))
            aDeck[k] = ( i , j )
    k += 1



# iList = range(2)
# jList = range(3)
# kList = range(5)

# for i in iList:
#     for j in jList:
#         print("i =",i ,"j =",j ,"k =",k)




aDeckJson = json.dumps(aDeck,indent=4)
print("\naDeck後 =",aDeck)



print(card1.figure,"of",card1.suit)

k=["k1","k2","k3"]
joink="".join(k)

joink.count("1")

"".join(k).count("1")


'''
class MyClass:
    "A simple example class"
    i = 12345
    def f(self ,x):
        return 'hello world'



a = MyClass.i
print(a)

b = x.f
print(b)

k=0
xf = x.f
while k <= 5:
    print xf()
    k += 1

'''