

# import operator
# import string
print( "1.bin(9) =" ,bin(9) )

# print( "2.int(9,2) =" ,int(1000,2) )
# print(fac(3))


from functools import reduce 

def add2( a ,b ):
    return a +b

def add3( a ,b ,c ):
    return a +b +c

def add30( a ,b ,c=0 ):
    return a +b +c

def add35( a ,b ,c=5 ):
    return a +b +c



def multi( a ,b ):
    return a*b

def multi3( a ,b ,c=0 ):
    return a*b*c


def fac(x):
    return reduce( multi ,range( 1 ,x+1 ) )



# 做連加
print( "add2 =" ,reduce( add2 ,range(1,6) ))   # [1 ,5]

# 三變數是不能連加的，reduce一次只扔兩個變數，可是add3想要一次吃三個
# print( "add3 =" ,reduce( add3 ,range(1,6) ))   # [1 ,5]
'''reduce
取得a ,b
s0 =  0 +a =  0 +a
---------------------- 
s1 = s0 +b =  a +b
s2 = s1 +c = s1 +c
s3 = s2 +d = s2 +d
---------------------- 最後是給出 s1 +s2 +s3
'''

# 除非你讓 add3第三變數可以預設為0，那麼reduce一次吃三個也就可以運作
print( "add30 =" ,reduce( add30 ,range(1,6) ))   # [1 ,5]


# 觀察他一次吃三個是怎麼運作的
print( "add35 =" ,reduce( add35 ,range(1,6) ))   # [1 ,5]
'''reduce
取得a ,b
s0 = (  0 +a ) +5 = (  0 +1 )
-------------------------------------
s1 = ( s0 +b ) +5 = (  1 +2 ) +5
s2 = ( s1 +c ) +5 = (  3 +3 ) +5
s3 = ( s2 +d ) +5 = (  6 +4 ) +5
s4 = ( s3 +e ) +5 = ( 10 +5 ) +5
------------------------------------- 最後是給出 s1 +s2 +s3
'''



# 因為reduce一段乘法
print( "multi =" , reduce( multi ,range(1 ,4) ))

# 就變成連乘，就變成階乘
print( "fac =" , fac(3) )


# 因為reduc一段乘法
print( "multi3 =" , reduce( multi3 ,range(1 ,4) ))

