

# 上層路徑設定
bottomPathHome = r"D:\GIT_Tortoise_Jumi_NB\HeadFirst_Python"
bottomPathOffice = r"C:\Users\Jumi_Hsu\Desktop\TortoiseGit_Jumi_jfi\HeadFirst_python"

# 檔案夾位置設定
btmPath = bottomPathHome
fileFolder = r"/chapter7_web"  # /webapp

# 匯入modual
import os
import sys
import pickle  # 需要讀檔+輸出檔案
sys.path.append(btmPath + "/openTxt")
sys.path.append(btmPath + "/athleteList")
import openTxt
import athleteList


# 變更工作路徑
openTxt.changechdir(btmPath, fileFolder)



# 關於Template：https://www.basemu.com/python3-4_template.html
# 匯入一個 Template 類，方便我們設定模板，用以套入可變字串
from string import Template



# 可用於創建一個CGI"content-type:"行
def start_response(resp="text/html"):
    return('Content-type: ' + resp + '\n\n')


# 打開指定的html模板文件，讀取此文件，並將標題替換成 輸入的指定內容 (the_title)
# substitute函數：需要一個string做為參數，用在html頁面最前面的標題中
# 頁面本身儲存在一個單獨的文件 "templates/header.html"中，可以根據需要替換標題
def include_header(the_title):
    # with open('templates/header.html') as headf:
    with open('webapp/templates/header.html') as headf:
        head_text = headf.read()
    header = Template(head_text)
    return(header.substitute(title=the_title))


# 打開指定的html模板文件，讀取此文件，並將連結替換成 the_links中 提供的HTML連結字典
# (輸入the_links，並重複+=回link_string)
def include_footer(the_links):
    # with open('templates/footer.html') as footf:
    with open('webapp/templates/footer.html') as footf:  # 不定義工作區域這邊沒辦法讀
        foot_text = footf.read()
    link_string = ''

    for key in the_links:
        # 將連結字典轉換為一個string，並換入模板
        # '</a>&nbsp;&nbsp;&nbsp;&nbsp;'
        # 雖然有點怪異，但這是html在string中加入空格的強制做法
        link_string += '<a href="' + the_links[key] + '">' + key + '</a>&nbsp;&nbsp;&nbsp;&nbsp;'
    footer = Template(foot_text)

    # substitute函數：與 include_header 類似，需要一個string做為參數，用在html頁面最後面的尾巴中
    # 頁面本身儲存在一個單獨的文件 "templates/footer.html"中
    # 參數則是拿來動態的創建一組 html 連結標記
    # 從標記的使用來看，此參數應該是一個字典
    return(footer.substitute(links=link_string))


# 返回表單最前面的html
# 允許調用者 指定url(表單數據將會發送到此URL)，亦可指定要使用的方法
def start_form(the_url, form_type="POST"):  # POST 或 GET
    return('<form action="' + the_url + '" method="' + form_type + '">')


# 返回 表單末尾 的HTML標記
def end_form(submit_msg="Submit"):
    return('<p></p><input type=submit value="' + submit_msg + '"></form>')


# html按鈕
def radio_button(rb_name, rb_value):
    return('<input type="radio" name="' + rb_name +
                             '" value="' + rb_value + '"> ' + rb_value + '<br />')


# html列表
def u_list(items):
    u_string = '<ul>'
    for item in items:
        u_string += '<li>' + item + '</li>'
    u_string += '</ul>'
    return(u_string)


# html標題
def header(header_text, header_level=2):
    return('<h' + str(header_level) + '>' + header_text +
           '</h' + str(header_level) + '>')


# html段落
def para(para_text):
    return('<p>' + para_text + '</p>') 



# ===================================================================
# 使用 html 模板
# ===================================================================
# '''
print("\n=== CGI標準：每一個 web request 都必須有一個首部行來指出，request中包含的數據類型 ===")
print(start_response())  # 後面會攜帶兩個換行符號\n\n
print(start_response("text/plain"))
print(start_response("application/json"))

print("\n=== 生成一個 web 頁面的開始部分，並允許訂製頁面的標題 ===")
print(include_header("Welcome to my home on the web!"))

print("\n=== 生成一個 web 頁面末端的 html，並提供連結(如果有提供連結的字典的話) ===")
print(include_footer(
    {'Home':'/index.html'
    ,'Select':'/cgi-bin/select.py'
    }))

print("\n=== 如果為空字典，就不包含連結html ===")
print(include_footer({}))

print("\n=== 會創建一個 html 表單，並可額外提供參數來調整所生成的 html 的內容 ===")
print(start_form("/cgi-bin/process-athlete.py"))

print(end_form())
print("\n",end_form("Click to confirm your order"))


print("\n=== 創建 html 單選按鈕 ===")
for fab in ["Jumi","Kao","Banana","Fionanna"]:
    print(radio_button(fab,fab))

print("\n=== 創建 html 無序列表 ===")
print(u_list(["Life of Brian","Holy Grail"]))

print("\n=== header()函數 快速建立選定級別的 html 標題 (預設=2) ===")
print(header("Welcome to my home on the web!"))
print(header("This is sub-sub-sub-sub heading",5))

print("\n=== 最後(但不是不重要)，para()會把一段文字，包夾在 html段落標記中 ===")
print(para("Was it worth the wait? \n We hope it was..."))

print("\n")
# '''


