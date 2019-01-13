# setup.py
from distutils.core import setup

setup(
    name='openTxt',
    version = '1.0.0',
    py_modules=['openTxt'],
    author = 'Jumi',
    author_email = 'scm80507211@gmail.com',
    url = '',
    description = '修改工作路徑至指定資料夾，讀取txt檔案'
    )


# 1
# 創建一個 def 檔 + setup檔，按照固定格式去設置 setup 檔
# 將上述 (a.py + setup.py) 放在共同的資料夾 A 下
# 到 資料夾路徑A 下，開啟cmd，輸入
# 指令：cd /d 右鍵貼上路徑
# setup.py sdist  (範例中是輸入： python3 setup.py sdist)
# a.py install    (範例中是輸入： sudo python3 setup.py install)
# 這時候會生出許多資料夾和檔案，發布已經就緒

# 2
# 使用他。
# 需要先定義該 module 所在位置
# import sys
# sys.path.append("C:/Users\***\***\****/nestPrint")
# import a
# 接著便可以 a.def() 去使用了!
