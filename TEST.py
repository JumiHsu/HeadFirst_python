# 各種TEST，雜記簿
from __future__ import unicode_literals

# python中要實現動態變數不像其它語言，可以通過 字串+變數(通常數字)，來達到動態變數。
# C語言例如
# for(i=0,i<5,i++){
# “abc”+i+”de”=1
# };
# 可達到abc0de=1；abc1de=1；abc2de=1；abc3de=1；abc4de=1

# 但是python要用：
for i in range(5):
    locals()["abc%s"%i + "de"] = 1
# 可達到abc0de=1；abc1de=1；abc2de=1；abc3de=1；abc4de=1

print(abc0de)
print(abc1de)
print(abc2de)
print(abc3de)
print(abc4de)
 
for i in ["a","b","c"]:
    locals()["abc%s"%i + "de"] = 2
    locals()["Element_%s"%i + "_is_"] = 3


print(abcade)
print(abcbde)
print(abccde)


print(Element_a_is_)
print(Element_b_is_)
print(Element_c_is_)




print("------------------------------------")
print("------------------------------------")

a="gg"

try:
    # b = int(a) * 2  # ValueError

    # b = a * 2 
    # print(int(b))     # ValueError

    print(b)            # NameError

except ValueError:
    print("ValueError")
except IOError:
    print("IOError")
except TypeError:
    print("TypeError")
except:
    print("Error")


# 也可放入兩個動態變量(例如i及j放入)
# for i in range(1,11):
#     j=9
#     locals()[“biosomeday%s%s” %( i , j )+”abc”]=3
#     print(locals()[“biosomeday%s%s” % ( i , j )+”abc”])

# 共 2046次被閱讀



'''
# 在 python 3中，這很容易

# 复制代码
myVariable = 5
for v in locals():
    if id(v) == id("myVariable"):
        print(v, locals()[v])
        
# 這將列印：
# myVariable 5
'''



'''
some= 1
list= 2
of= 3
vars= 4

a = dict( (name,eval(name)) for name in ['some','list','of','vars'] )
print(a)
'''




print("\n\n")



'''
def details(val):
    vn = val.__name__          # If such a thing existed
    vs = str(val)
    print("The Value of"+ str(vn) +" is" + vs)
    print("The data type of" + vn +" is" + str(type(val)))

m = 'abracadabra'
mm=[] 
for n in m:
    mm.append(n)

mydic = {'first':(0,1,2,3,4,5,6),'second':mm,'third':3}
details(mydic)
'''

'''
myVariable = 5
for v in locals():
    if id(v) == id("myVariable"):
        print(v, locals()[v])
'''





'''
a=1
for k, v in list(locals().iteritems()):
    if id(v) == id(a):
        a_as_str = k

print("a=",a,"a_type =",type(a))
'''



