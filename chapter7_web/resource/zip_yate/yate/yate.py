
# 關於Template：https://www.basemu.com/python3-4_template.html
# 匯入一個 Template 類，方便我們設定模板，用以套入可變字串
from string import Template


# 可用於創建一個CGI"content-type:"行
# 需要一個string參數(optional，預設為"text/html")
def start_response(resp="text/html"):
    return('Content-type: ' + resp + '\n\n')


# 打開指定的html模板文件，讀取此文件，並將標題替換成 輸入的指定內容 (the_title)
# substitute函數：需要一個string做為參數，用在html頁面最前面的標題中
# 頁面本身儲存在一個單獨的文件 "templates/header.html"中，可以根據需要替換標題
def include_header(the_title):
    with open('templates/header.html') as headf:
        head_text = headf.read()
    header = Template(head_text)
    return(header.substitute(title=the_title))


# 打開指定的html模板文件，讀取此文件，並將連結替換成 the_links中 提供的HTML連結字典
# (輸入the_links，並重複+=回link_string)
def include_footer(the_links):
    with open('templates/footer.html') as footf:
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
# 並允許調用者 訂製表單按鈕"submit"的文字顯示內容
def end_form(submit_msg="Submit"):
    return('<p></p><input type=submit value="' + submit_msg + '"></form>')


# 創建並定義一個單選的button，名和值
def radio_button(rb_name, rb_value):
    return('<input type="radio" name="' + rb_name +
                             '" value="' + rb_value + '"> ' + rb_value + '<br />')


# 生成一系列的項目列表，轉變成html的無序列表(使用for循環)
# 每次迭代都會對ul元素生成一個新的li元素
def u_list(items):
    u_string = '<ul>'
    for item in items:
        u_string += '<li>' + item + '</li>'
    u_string += '</ul>'
    return(u_string)


# 創建一個html標題標記(H1 H2 H3等)，預設字級為2，並定義標題內容
def header(header_text, header_level=2):
    return('<h' + str(header_level) + '>' + header_text +
           '</h' + str(header_level) + '>')


# 用html段落標記，包圍一段文字(string)。是否有點沒必要?
def para(para_text):
    return('<p>' + para_text + '</p>') 
