# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 10:57:20 2020

@author: p35k
"""
import time
from mcpi.minecraft import Minecraft
#連結 mcpi 資料夾
mc=Minecraft.create()
#連結Minecraft

while True:
    #執行迴圈
    x,y,z=mc.player.getTilePos()
    #設定 x y z 變數為玩家座標
    mc.postToChat("x="+str(x)+" y="+str(y)+" z="+str(z))
    #顯示玩家座標   "x="str(x) 將數字轉成文字
    time.sleep(0.5)
    #等待 0.5 秒