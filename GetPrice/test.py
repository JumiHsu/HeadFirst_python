# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 22:47:55 2018

@author: SCM80
"""
loading=3
import time

def matching():
    level=input("what rank would you want? (hard/medium/easy)")
    game_min=input("OK! how long do you want? (5/10/20 min)")
    print("準備牌桌...")
    time.sleep(loading-1)
    print("觀眾入座...")
    time.sleep(loading-2)
    print("辣的要命的店員給每個人遞上啤酒...")
    time.sleep(loading)
    print("洗牌並發牌...")
    time.sleep(loading+1)
    print("來吧! 限時",game_min,"分鐘! 一場精采的",level,"級挑戰賽，就要開始了!")


print("歡迎光臨，你想要開始一場比賽嗎?")
ans=input("Y/N")
if ans=="Y":
    matching()
else: print("沒問題! 期待下次看到你!")
pass
    