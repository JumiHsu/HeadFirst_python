
# 關於 Lambda 的一些看得懂或看不懂的小筆記


# 用 def
def add1(x):
    return x+1
    
# 用 lambda
add2 = lambda x:x+2

# 驗證
print( "3 + 1 =" ,add1(3) )
print( "3 + 2 =" ,add2(3) )



li=[]
for x in range(5):
    li.append(lambda x: x**2)

print( li[0](2) ) # 4
print( li[1](3) ) # 9

print( li[0] ) # <function <lambda> at 0x0508B198>
print(li)
'''
[
<function <lambda> at 0x04B101E0>
,<function <lambda> at 0x04B10228>
,<function <lambda> at 0x04B10270>
,<function <lambda> at 0x04B102B8>
,<function <lambda> at 0x04B10300>
]
'''