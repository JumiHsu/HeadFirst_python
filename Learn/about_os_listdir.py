'''參考來源
5.13 获取文件夹中的文件列表
https://python3-cookbook.readthedocs.io/zh_CN/latest/c05/p13_get_directory_listing.html#
'''
somePath = "D:\GIT_Tortoise_Jumi_NB\HeadFirst_Python\chapter7_web"

# 基本語法
import os
names = os.listdir(somePath)
print("\n",names)

# Get all regular files. (撈出是檔案的人，成為一個list)
import os.path
names = [name for name in os.listdir(somePath) 
if os.path.isfile(os.path.join(somePath,name))]
print("\n",names)

# Get all dirs
dirnames = [name for name in os.listdir(somePath) 
if os.path.isdir(os.path.join(somePath,name))]
print("\n",dirnames)


# Get all .py files
pyfiles = [name for name in os.listdir(somePath) 
if name.endswith(".py")]
print("\n",pyfiles)  # 返回符合條件的檔案，的檔案名

webMVCfiles = [name for name in os.listdir(somePath) 
if name.startswith("webMVC")]
print("\n",webMVCfiles)


import glob
pyfiles = glob.glob(somePath+"/*.py")
print("\n",pyfiles)  # 返回符合條件的檔案，的完整路徑(包含檔案名)


# Test whether FILENAME matches PATTERN
from fnmatch import fnmatch
pyfiles = [name for name in os.listdir(somePath) 
if fnmatch(name, '*.py')]