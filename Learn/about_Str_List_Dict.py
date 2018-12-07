


# ===================================================================
# 製作一個 value=tuple 的dict
# ===================================================================
# https://blog.gtwang.org/programming/python-iterate-through-multiple-lists-in-parallel/

key=["a","b","c","d"]

a1=["A","B","C","D"]
a2=["AA","BB","CC","DD"]
a3=["AAA","BBB","CCC","DDD"]
temp=[]

for x, y, z in zip(a1, a2, a3):
    temp.append((x,y,z))
    print(x, y, z)
    print(temp)

a=dict( zip(key,temp) )
print("a=",a)





# ========================================================================
# 把變數名稱當成字串
# ========================================================================
variable_test = 1
print( "list =",[k for k,v in locals().items() if v is variable_test] )
# list = ['abc0de', 'abc1de', 'abc2de', 'abc3de', 'abc4de', 'variable_test']

variable_name = [
    k for k,v in locals().items()
    if v is variable_test
    ][0]

print("variable_name =",variable_name)

'''
14:36 高謙 通常撈Dictionary的資料會這樣用
14:36 高謙
for k,v in DICTIONARY:
    if v is ABC:
        return k, v
14:36 高謙 類似這樣
14:36 高謙 k就是dictionary裡的key值 v是dictionary裡的value
14:39 高謙 用迴圈去遍歷這個Dictionary裡面的資料 再看要比對的是key還是value值 用if去確認

'''




# ========================================================================
# 不需要浪費變數空間，也可以print東西
# ========================================================================
dictTest = {'Name': 'Zara', 'Age': 7}

print( "Value : %s" %  dictTest.keys()  )
# Value : dict_keys(['Name', 'Age'])
print("可以嗎=",dictTest.keys())
print("這樣呢=",dictTest.items())


# https://openhome.cc/Gossip/Python/StringFormat.html

a='{0} is {1}!!'.format('Justin', 'caterpillar')
print(a)     # 'Justin is caterpillar!!'
a='{real} is {nick}!!'.format(real = 'Justin', nick = 'caterpillar')
print(a)     # 'Justin is caterpillar!!'
a='{real} is {nick}!!'.format(nick = 'caterpillar', real = 'Justin')
print(a)     # 'Justin is caterpillar!!'
a='{0} is {nick}!!'.format('Justin', nick = 'caterpillar')
print(a)     # 'Justin is caterpillar!!'
a='{name} is {age} years old!'.format(name = 'Justin', age = 35)
print(a)     # 'Justin is 35 years old!'




import math
a='PI = {0.pi}'.format(math)
print(a)     # PI = 3.141592653589793

import sys
a= 'My platform is {pc.platform}'.format(pc = sys)
print(a)     # My platform is win32

a= 'My platform is {0.platform}. PI = {1.pi}.'.format(sys, math)
print(a)     # My platform is win32. PI = 3.141592653589793.

a= 'element of index 1 is {0[1]}'.format([20, 10, 5])
print(a)     # element of index 1 is 10

a= 'My name is {person[name]}'.format(person = {'name' : 'Justin', 'age' : 35})
print(a)     # My name is Justin

a= '{person}'.format(person = {'name' : 'Justin', 'age' : 35})
print(a)     # {'name': 'Justin', 'age': 35}


# print('{person.items}'.format(person = {'name' : 'Justin', 'age' : 35}))
# print('{person.key}'.format(person = {'name' : 'Justin', 'age' : 35}))








# ========================================================================
# 以下為還不是很理解的
# ========================================================================
def runoob(arg):    # 两个局部变量：arg、z
    z = 1
    print( locals() )
    # a=locals()
    # print( a[arg] )

print(runoob(4))
# {'arg': 4, 'z': 1}      # 返回一个名字/值对的字典
# print(runoob(4)[0])     # 這樣會報錯




# ========================================================================
import binascii

a = 'runoob'
print( "id(a) =",id(a) )          # 74471616
print( "hex(id(a))=",hex(id(a)) ) # 0x47058c0

print ( binascii.a2b_hex("e4bda0e5a5bde5958a").decode("utf8")   )
# print ( binascii.a2b_hex("0x47058c0").decode("utf8") )
# a.strip().decode('hex')


# a = 'helloworld'
print( binascii.b2a_hex(u"你好啊".encode("utf8"))   )
print( binascii.a2b_hex("e4bda0e5a5bde5958a").decode("utf8")   )

# b = binascii.b2a_hex(a)  
# print(b)  
# b'68656c6c6f20776f726c64'  
# b = binascii.hexlify(a)  
# print(b)  
# b'68656c6c6f20776f726c64'  
# print(binascii.unhexlify(b))  
# b'hello world'  
