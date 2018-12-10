
# import os

# print("當前工作路徑=", os.getcwd())
# # os.chdir("D:\GIT_Tortoise_Jumi_NB\HeadFirst_Python\ReadFile")
# os.chdir("C:/Users/Jumi_Hsu/Desktop/TortoiseGit_Jumi_jfi/HeadFirst_python/nestPrint")
# print("當前工作路徑=", os.getcwd())


import sys
sys.path.append("C:/Users\Jumi_Hsu\Desktop\TortoiseGit_Jumi_jfi\HeadFirst_python/nestPrint")
import nestPrint                                     # 這樣沒報錯，但一樣跳error


# 如果是一個，表中表中表的話呢?
movie = ["片名：La la Land",2016,"導演：Damien Chazelle",
        ["主演1：Sebastian Wilder","主演2：Mia Dolan","主演3：Keith",
        ["音樂：Justin Hurwitz","編劇：Damien Chazelle"]]]

nestPrint.identifyType_nestPrint(movie)




'''
******** 同一文件目录下 ********
在b.py文件中用下面两条语句即可完成对a.py文件中func( )函数的调用

import a #引用模块 
a.func( )

或者是

import a#应用模块 
from a import func #引用模块中的函数 
func（） #这里调用函数就不需要加上模块名的前缀了




******** 不同文件目录下 ********
若不在同一目录，python查找不到，必须进行查找路径的设置，将模块所在的文件夹加入系统查找路径

import sys 
sys.path.append(‘a.py所在的路径’) 
import a 
a.func()
--------------------- 
作者：HelloWorld_EE 
来源：CSDN 
原文：https://blog.csdn.net/u010412719/article/details/47089883 
版权声明：本文为博主原创文章，转载请附上博文链接！
'''
