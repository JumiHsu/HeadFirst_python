
# 匯入modual
import cgi
import athletemodel
import yate
import cgitb
cgitb.enable()

# 從模型得到數據，...這裡跟下面那段有什麼不同?
athletes = athletemodel.get_from_store()
'''
import glob
data_files = glob.glob("data/*.txt")
athletes = athletemodel.put_to_store(data_files)
'''


'''你在處理哪一個選手的數據'''
# 使用cgi.FieldStorage() 访问web请求发送给web服务器的数据，这些数据为一个Python字典
# https://www.cnblogs.com/windlaughing/p/3153848.html
# 這裡的數據指的是 athletes 這個數據 (字典，index=選手名，值=一個list特徵的物件)
form_data = cgi.FieldStorage() # 我還是不太清楚 form_data是個什麼東西

# 在 generate_list 中，我們作的button，
# 把 "which_athlete"塞到 name，把選手的名字=athletes[each_athlete].name塞到value
# 即：
# <input type="radio" name="which_athlete" value="選手名字"> 選手名字<br />
athlete_name = form_data["which_athlete"].value



# 總是以 Content-type 作為開頭
print(yate.start_response())
# 生成webPage並提供標題
print(yate.include_header("指定選手的計時數據"))
print(yate.header("選手:" + athlete_name + 
                  ",生日:" + athletes[athlete_name].birth + "。"))



# 接下來才是內容段落：告訴妳的用戶要作什麼
print(yate.para("The top times for this athlete are:"))
# 生成一個無序的list
print(yate.u_list(athletes[athlete_name].top3))  # 有@property
# print(yate.u_list(athletes[athlete_name].top3())) # 沒有@property

# 在生成的HTML頁面最下面增加一個連結，指向主頁Home
print(yate.include_footer({"Home":"/index.html",
                           "Select another athlete":"generate_list.py"}))

