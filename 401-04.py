# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 10:00:07 2020

@author: p35k
"""
import time
from mcpi.minecraft import Minecraft
mc=Minecraft.create()


while True:
    x,y,z=mc.player.getTilePos()
    a = mc.getBlock(x+1, y-1, z)
    b = mc.getBlock(x, y-1, z+1)
    c = mc.getBlock(x-1, y-1, z)
    d = mc.getBlock(x, y-1, z-1)
    if(a == 8 or a==9):mc.setBlocks(x+1, y-1, z+1, x-1, y-1, z-1, 2)
    if(b == 8 or b==9):mc.setBlocks(x+1, y-1, z+1, x-1, y-1, z-1, 2)
    if(c == 8 or c==9):mc.setBlocks(x+1, y-1, z+1, x-1, y-1, z-1, 2)
    if(d == 8 or d==9):mc.setBlocks(x+1, y-1, z+1, x-1, y-1, z-1, 2)
    mc.setBlock(x, y, z, 38)
    time.sleep(0.1)
    