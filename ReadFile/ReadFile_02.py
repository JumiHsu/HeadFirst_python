import os
# 確認當前的工作路徑
print("當前工作路徑=",os.getcwd())

# 檔案要放在工作路徑下
result_f01=open("result01.txt")
print(result_f01)

# 如果要變更工作路徑：os.chdir('the dir which include the file a.txt') #修改当前工作目录
os.chdir("D:\GIT_Tortoise_Jumi_NB\HeadFirst_Python\ReadFile")
# 再讀一次檔案看看
result_f02=open("result02.txt")
print(result_f02)

print("變更當前工作路徑=",os.getcwd())

# ===============================================
# 尋找最高分 (取用 result_f02)
# ===============================================

highest_score=0

# 需要處理空白字元做分隔的資料
# 可以用result_f02.find(" ")來尋找空白字元，也可以使用split()
# 寫法：(變數名稱1, 變數名稱2)=以空白分隔的行資料.split()
for line in result_f02:

    (name,score)=line.split()    # 特別留意，對象是line而非result_f02
    
    if float(score) > highest_score:
        highest_score=float(score)


result_f02.close()

print("\n")
print("最高分=",highest_score)

# ============================================
# 但如果是要找出前三高分的話呢（學習使用array）
# ============================================

my_words = ["Jumi","KaoChin"]
print(my_words)
