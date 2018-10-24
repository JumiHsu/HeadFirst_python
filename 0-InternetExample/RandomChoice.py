# Numpy隨機抽樣之抽出不放回統計作圖
import numpy as np
import matplotlib.pyplot as plt
import seaborn
seaborn.set()
# -----
pops = np.random.randint(1,21, size=(10, 2))
print("pops母體樣本點(100點) :\n", pops)
# -----
# 利用randint隨機產生值1-20之100x2二維陣列
# 註：陣列註標索引之起始值為0，要小心!!
# -----
indices = np.random.choice(10, 20, replace=False)
# -----
# np.random.choice代表隨機抽樣之意，0-99中抽出20個樣本，且
# 抽樣後不放回(replace=False，因此不重複抽樣)
# -----
print("\nindices索引值(隨機20組) :", indices, "\n")
samplePoints = pops[indices]
print("母體數100點隨機抽出20組樣本 :\n", samplePoints)
plt.scatter(samplePoints[:, 0], samplePoints[:, 1])

# -----
# 調用scatter產生散點圖
# 相當於plt.scatter(samplePoints[0:20, 0], samplePoints[0:20, 1])
# 列的部分使用: => 代表所有的列。而scatter出20個點，則是利用numpy
# 陣列的廣播(broadcast)技巧
# 比方：scatter(samplePoints[0, 0], samplePoints[0, 1])
# 就是到samplePoints二維矩陣擷取[0,0]及[0,1]兩元素值分別作為
# 散點圖中第1點的x,y軸座標值
# -----

'''
執行：
pops母體樣本點(100點) :
 [[10  1]
 [ 8 13]
 [ 6  8]
 [ 8 12]
 [10 14]
 [13 18]
 [17 20]
 [ 1  9]
 [16  5]
 [ 7 16]
 [12  9]
 [20  1]
 [ 8  6]
 [18 17]
 [19 10]
 [20  2]
 [19  9]
 [11  1]
 [20 16]
 [10  8]
 [10  4]
 [ 2 11]
 [12  2]
 [10  2]
 [ 3 11]
 [ 9  2]
 [20 13]
 [10  3]
 [17 13]
 [ 3 14]
 [ 2 16]
 [ 7  3]
 [17  2]
 [19 18]
 [11 17]
 [10 10]
 [18  8]
 [ 8  9]
 [ 6  5]
 [ 7  9]
 [ 9 20]
 [16  5]
 [20 16]
 [15 15]
 [11 10]
 [ 1 18]
 [18  7]
 [19 18]
 [17  1]
 [14  2]
 [ 4 18]
 [15 13]
 [10 19]
 [ 6  3]
 [20  5]
 [ 2 19]
 [ 2  6]
 [ 8 15]
 [16  7]
 [ 2 20]
 [ 8  3]
 [ 2  3]
 [ 2 10]
 [ 5 11]
 [17  5]
 [ 1  7]
 [ 4 11]
 [18 16]
 [12 10]
 [ 5  4]
 [ 1 10]
 [ 4  8]
 [13  5]
 [15 16]
 [14  6]
 [ 9 19]
 [ 8  7]
 [11 18]
 [14 18]
 [ 5  1]
 [ 9 20]
 [ 2 20]
 [14  1]
 [19  2]
 [17 12]
 [ 1 20]
 [ 6  8]
 [ 7 11]
 [ 5  2]
 [ 4 12]
 [15  6]
 [17  6]
 [15  1]
 [ 4 20]
 [16  7]
 [ 4 18]
 [ 7 10]
 [19  6]
 [ 8 20]
 [ 4 17]]

indices索引值(隨機20組) : [88 64 47  6 10 65 28 98 77 32 86 25 72 38 62 91 16 73 56 63]

母體數100點隨機抽出20組樣本 :
 [[ 5  2]
 [17  5]
 [19 18]
 [17 20]
 [12  9]
 [ 1  7]
 [17 13]
 [ 8 20]
 [11 18]
 [17  2]
 [ 6  8]
 [ 9  2]
 [13  5]
 [ 6  5]
 [ 2 10]
 [17  6]
 [19  9]
 [15 16]
 [ 2  6]
 [ 5 11]]
 '''