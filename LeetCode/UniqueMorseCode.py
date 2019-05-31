'''
International Morse Code defines a standard encoding
where each letter is mapped to a series of dots and dashes,
as follows: "a" maps to ".-", "b" maps to "-...", "c" maps to "-.-.", and so on.

For convenience, the full table for the 26 letters of
the English alphabet is given below:

[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

Now, given a list of words, each word can be written
as a concatenation of the Morse code of each letter.
For example, "cba" can be written as "-.-..--...",
(which is the concatenation "-.-." + "-..." + ".-").
We'll call such a concatenation, the transformation of a word.

Return the number of different transformations among all words we have.

Example:
Input: words = ["gin", "zen", "gig", "msg"]
Output: 2
Explanation: 
The transformation of each word is:
"gin" -> "--...-."
"zen" -> "--...-."
"gig" -> "--...--."
"msg" -> "--...--."

There are 2 different transformations, "--...-." and "--...--.".

Note:
The length of words will be at most 100.
Each words[i] will have length in range [1, 12].
words[i] will only consist of lowercase letters.

input四個字串，將他們轉成摩斯密碼
最後output相異的摩斯密碼有幾個
'''

MorseCode = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....",
             "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.",
             "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-",
             "-.--", "--.."]
Letters = ["a", "b", "c", "d", "e", "f", "g", "h",
            "i", "j", "k", "l", "m", "n", "o", "p",
            "q", "r", "s", "t", "u", "v", "w", "x",
            "y", "z"]

inputWord = ["gin", "zen", "gig", "msg"]

'''
outputMorseCode = []
for each in inputWord:
    tempMorse = []
    for i in range(len(each)):
        LettersIndexOf_each_i = Letters.index(each[i])
        # print("LettersIndexOf_each_i", LettersIndexOf_each_i,"\n")
        tempMorse.append(MorseCode[LettersIndexOf_each_i])
    print("第{0}個字串：{1}，\n轉換後的摩斯密碼為：\n{2}\n".format(i,each,tempMorse))
    outputMorseCode.append("".join(tempMorse))

print("最終的{0}個摩斯密碼為：\n{1}\n".format(len(inputWord), outputMorseCode))

# 方法3
# set={}
print("最終的不重複摩斯密碼為：\n", set(outputMorseCode))

# 注意排序完會變成 list=[]
print("(使用key排序) 最終的不重複摩斯密碼為：\n",
      sorted(set(outputMorseCode), key=outputMorseCode.index))

# 檢查type
print(type(sorted(set(outputMorseCode), key=outputMorseCode.index)))

# 回答問題
output=len(sorted(set(outputMorseCode), key=outputMorseCode.index))
print("output", output)

'''



'''

outputMorseCode = []
for each in inputWord:
    tempMorse = []
    for i in range(len(each)):
        LettersIndexOf_each_i = Letters.index(each[i])
        # print("LettersIndexOf_each_i", LettersIndexOf_each_i,"\n")
        tempMorse.append(MorseCode[LettersIndexOf_each_i])
    print("第{0}個字串：{1}，\n轉換後的摩斯密碼為：\n{2}\n".format(i,each,tempMorse))
    outputMorseCode.append("".join(tempMorse))

print("最終的{0}個摩斯密碼為：\n{1}\n".format(len(inputWord), outputMorseCode))

'''

def UniqueMorseRepresentations(inputWord, MorseCode, Letters):
    outputMorseCode = []
    for each in inputWord:
        
        tempMorse = []
        for i in range(len(each)):
            LettersIndexOf_each_i = Letters.index(each[i])
            # print("LettersIndexOf_each_i", LettersIndexOf_each_i,"\n")
            tempMorse.append(MorseCode[LettersIndexOf_each_i])

        print("字串：{0}，轉換後的摩斯密碼為：\n{1}\n".format(each, tempMorse))
        outputMorseCode.append("".join(tempMorse))

    # 全部的轉換結果
    print("轉換後的ALL摩斯密碼為：\n", outputMorseCode)

    # set={}
    print("最終的不重複摩斯密碼為：\n", set(outputMorseCode))
    # 注意排序完會變成 list=[]
    print("(使用key排序) 最終的不重複摩斯密碼為：\n",
    sorted(set(outputMorseCode), key=outputMorseCode.index))
    # outputMorseCode.append("".join(tempMorse))
    output = len(sorted(set(outputMorseCode), key=outputMorseCode.index))
    print("output =", output)

    return(output)


UniqueMorseRepresentations(inputWord, MorseCode, Letters)

'''
【去除重複】
方法1，對列表呼叫排序，從末尾依次比較相鄰兩個元素，遇重複元素則刪除，否則指標左移一位重複上述過程
方法2，設一臨時列表儲存結果，從頭遍歷原列表，如臨時列表中沒有當前元素則追加
方法3，利用python中集合元素惟一性特點，將列表轉為集合，將轉為列表返回

方法1，邏輯複雜，臨時變數儲存值消耗記憶體，返回結果破壞了原列表順序，效率最差
方法2，直接呼叫append方法原處修改列表，邏輯清晰，效率次之
方法3，極度簡潔，使用python原生方法效率最高

https://codertw.com/%E7%A8%8B%E5%BC%8F%E8%AA%9E%E8%A8%80/362696/
'''




