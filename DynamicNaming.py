
'''
動態命名變數

參考資料：
http://blog.hhjh.tn.edu.tw/biosomeday/?p=607
http://yhhuanglab.blogspot.com/2016/01/python.html
'''

print("11 -----------------------------------")
for i in range(5):
    locals()["abc%s" %i + "de"] = 1
# 產生變數：abc0de=1；abc1de=1；abc2de=1；abc3de=1；abc4de=1


print("12 -----------------------------------")
for i in range(1,10):
    j=9
    locals()["biosomeday%s%s" %( i , j ) + "abc" ] = 3
    print(locals()["biosomeday%s%s" % ( i , j ) + "abc" ])


print("21 -----------------------------------")
for i in range(0,3):
    locals()['X%s' % (i)]=i
    print('X'+str(i)+'='+ str(locals()['X%s' % (i)]))

print("22 -----------------------------------")
# 其中也顯示了int轉換成string的兩種方法
# 發生 TypeError: Can't convert 'int' object to str implicitly 錯誤

#coding:utf-8
people = 3
print('%s' % (people)+'人成虎')

#coding:utf-8
people = 3
print(str(people)+'人成虎')

