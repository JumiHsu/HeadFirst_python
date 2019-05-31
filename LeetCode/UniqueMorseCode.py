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
outputMorseCode = []

for each in inputWord:
    tempMorse = []
    for i in range(len(each)):
        LettersIndexOf_each_i = Letters.index(each[i])
        # print("LettersIndexOf_each_i", LettersIndexOf_each_i,"\n")
        tempMorse.append(MorseCode[LettersIndexOf_each_i])
    print("第{0}個字串：{1}，\n轉換後的摩斯密碼為：{2}\n".format(i,each,tempMorse))
    outputMorseCode.append("".join(tempMorse))

print("最終的{0}個摩斯密碼為：{1}\n".format(len(inputWord), outputMorseCode))





