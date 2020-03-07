# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 02:27:40 2020

@author: 學生
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create();
pos= mc.player.getTilePos()
print(pos)
x = 100
y = 100
z = 100
mc.player.setTilePos(100,100,100)
