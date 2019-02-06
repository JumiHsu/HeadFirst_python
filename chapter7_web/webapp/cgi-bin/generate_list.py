
# 匯入modual
import athletemodel
import yate
import glob
import cgitb
cgitb.enable()

# 他是讀取相對路徑? (看起來他是自動抓 以cgi-bin上層 為基礎路徑)
data_files = glob.glob("data/*.txt")
athletes = athletemodel.put_to_store(data_files)
'''athletes是一個字典，index是選手的name，
內容物是一個具有額外屬性的list繼承物件，所以可以用dict["index"].birth來呼叫一些屬性
而他自己也可以被extend新的time資料，因為他本身繼承自list
'''


# 總是以 Content-type 作為開頭
print(yate.start_response())
# 生成webPage並提供標題
print(yate.include_header("Coach Kelly's List of Athletes"))
# 開始生成表單，並提供要連接的服務器端程序的名字
print(yate.start_form("generate_timing_data.py"))


# 接下來才是內容段落：告訴妳的用戶要作什麼
print(yate.para("Select an athlete from the list to work with:"))
# 生成各選手表單按鈕
for each_athlete in athletes:  # each_athlete 是字典的index，也就是選手的name
    print(yate.radio_button("which_athlete",athletes[each_athlete].name))
# 表單的最後提供一個按鈕Select
print(yate.end_form("Select"))


# 在生成的HTML頁面最下面增加一個連結，指向主頁Home
print(yate.include_footer({"Home":"/index.html"}))
