
# https://pythonhow.com/start/
i=0

# Level 1
# What’s the 101st character of the text?
target = "Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient python, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, baxa quouq. axa la consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Proin at neque et tellus ultricies consequat. Duis vitae mi commodo, suscipit nunc vel, porta tellus. In eu volutpat sapien. Mauris dignissim velit eget diam tristique, nec egestas magna maximus. Pellentesque python, lorem a eleifend vehicula, arcu urna facilisis odio, maximus maximus massa nisl sed sapien. Quisque nisi nunc, dignissim ut malesuada non, fringilla vitae sem. Nunc turpis quam, rutrum at egestas ut, pretium tincidunt est. Praesent imperdiet mauris eu felis lobortis vehicula. Sed dictum lorem at rutrum rhoncus. Suspendisse sit amet ex ac eros python cursus. Duis pretium rutrum lacus, sit amet vulputate ipsum condimentum vel. Vivamus lacus ipsum, python in justo quis, blandit condimentum velit esed semper posuere leo, elementum tristique leo euismod quis."
i += 1
print("\n",i,".",target[100])




# https://pythonhow.com/start/t
# Level 2
# 承上，The middle character
# middle = 奇數時，位置=除2取整+1，但字串從0起算，所以位置=除2取整
i += 1
if len(target)%2 == 0:
    print("\n",i,".","plz Check.")
else:
    print( "\n",i,".",target[ int(len(target)/2) ] )



# https://pythonhow.com/start/x
# Level 3
# 承上，The three middle character，中間三個字符
i += 1
takeNum = 3
halfNum = int(takeNum/2)
print("\n",i,".",
    target[
        int(len(target)/2)-halfNum :
        int(len(target)/2)+halfNum+1
        ]
        )
''' Tip
text="1234567"
print( text[2 : 5] )
print(int(len(text)/2)-halfNum) # 中間位置 - 取整(取用字符數/2) = 開始位置
print(int(len(text)/2)+halfNum) # 中間位置 + 取整(取用字符數/2) = 結束位置
# 但因為他取左不取右，所以要 + 1
print(int(len(text)/2)+halfNum+1) # 中間位置 + 取整(取用字符數/2)+1
'''

# https://pythonhow.com/start/axa
# Level 4
# 承上，先獲得此文章總字數，
# 並藉由 0->a, 1->b, ...的字符轉換關係，取得下一階段關鍵字
i += 1

targetCharacterTotal = len(target)
targetCharacterTotalStr = str(targetCharacterTotal)
print("\n文章總長度 =",targetCharacterTotal)

alphabetSmallList = [chr(i) for i in range(97,122)]
print("alphabetSmallList =",alphabetSmallList)

index = 0
ans4=[]
while index < len(targetCharacterTotalStr):
    ans4.append( alphabetSmallList[ int(targetCharacterTotalStr[index]) ] )
    index += 1
# 63:TypeError
# list indices must be integers or slices, not str
# 解決：targetCharacterTotalStr[index]為一個str，但規格為 list[int]

print("\n",i,".","".join(ans4))





''' 生成數列 '''
serial1 =[k for k in range(0,26)]    # 一個list
serial2 ={k for k in range(0,26)}    # 結果他是一個set，不是dict
serial3 = dict.fromkeys(serial1, 0)                   # 這樣才是一個dict
serial4 = dict.fromkeys([k for k in range(0,26)], 0)  # 這樣才是一個dict
# print("serial4=",serial4,type(serial4))

''' 生成字母表，ASCII碼表，Dec碼為10進位碼 '''
A=[]
for i in range(65,91):                # 寫法 1 = ['A', 'B', 'C',..., 'Z']
    A.append(chr(i))

[chr(i) for i in range(97,123)]       # 寫法 2 = ['a', 'b', 'c',..., 'z']



''' 生成連續字串，用 "".join 就可以串在一起 '''
"".join( [chr(i) for i in range(65,91)] )   # 寫法 1 = ABCDEFG...WXYZ


''' string.ascii_lowercase本身就是連續字串 '''
import string
# print("string.ascii_lowercase =",string.ascii_lowercase)  # 寫法 2 = ab...xyz


''' 生成字典，直接取用 import string  '''
import string
for j in range(0,26):
    serial3[j] = string.ascii_lowercase[j]
# print("\nserial3 =",serial3)

''' 生成字典，直接取用 import string (但統一都被填入0)'''
dict.fromkeys(string.ascii_lowercase, 0)
# print("\ndict.fromkeys =",dict.fromkeys(string.ascii_lowercase, 0))






# https://pythonhow.com/start/bjbh
# Level 5
# 承上，找出這篇文章有幾個詞，並且此數字轉換為字母
i += 1
