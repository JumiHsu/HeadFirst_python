'''參考資料：
https://www.jianshu.com/p/3f72a18d484a
'''
import hashlib

# md5 摘要算法(非加密) (能加密就可以解密，摘要則是不可逆向的)
# 在同一台計算機上，跑多次答案會一樣；但不同台計算機則不同
md5 = hashlib.md5()
md5.update("123456".encode("utf-8"))
print("\nmd5 =", md5.hexdigest())
# 需要注意的是更新（update）hash对象的时候只能使用byte类型。
# 所以寫這樣也可以：md5.update(b"123456")


# sha1加密
# 在不同台計算機上，答案也一樣
sha1 = hashlib.sha1()
sha1.update("123456".encode("utf-8"))
print("\nsha1 =", sha1.hexdigest())


# salt加密
# 怕撞庫破解 (在不同台計算機上，答案也一樣)
salt = hashlib.md5("password".encode("utf-8"))
salt.update("123456".encode("utf-8"))
print("\nsalt =", salt.hexdigest())


'''參考資料：
https://www.xzymoe.com/python-hashlib/

原理：網站不能儲存用戶的密碼，所以只能透過儲存一個 單向函數 求得的結果
下次用戶輸入時，進行比對來通過驗證
但如果 A密碼→a，結果B密碼→a 也得到a的話，就撞庫了
'''
passwordEnterA = "fake12AA"  # 最大12碼英數混合有分大小寫
passwordEnterB = "fake12bbb"  # 最大12碼英數混合有分大小寫

salt.update(passwordEnterA.encode("utf-8"))
userA_password = salt.hexdigest()
print("userA的摘要資訊 =", userA_password)


