'''
在 Facebook 上面，對於按讚這個功能，通常會有以下幾種描述：

只有一個人按讚：A likes this
有兩個人按讚：A and B like this
有三個人按讚：A, B and C like this
有四個人以上按讚：A, B and 2 others like this

寫一個 function，會給你一個叫做 names 的陣列，根據 names 輸出結果。
'''

names0 = [ ]
names1 = [ "Jumi" ]
names2 = [ "Jumi" ,"Kaochin" ]
names3 = [ "Jumi" ,"Kaochin" ,"Bananana" ]
names4 = [ "Jumi" ,"Kaochin" ,"Bananana" ,"Fionanna" ]

def like(names):
    oneLikesSentence = "likes this"
    likeSentence = "like this"

    if len(names) <= 0:
        show = print("Be the first to",likeSentence)
    
    elif len(names) == 1 :
        show = print(names[0] ,oneLikesSentence)

    elif len(names) == 2 :
        show = print(names[0] ,"and" ,names[1] ,likeSentence)

    elif len(names) == 3 :
        show = print(names[0]+"," ,names[1] ,"and" ,names[2] ,likeSentence)

    else :
        show = print(names[0]+"," ,names[1] ,"and 2 others" ,likeSentence)

    return show


like(names4)