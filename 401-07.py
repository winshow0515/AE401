# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 10:27:38 2020

@author: p35k
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x,y,z=mc.player.getTilePos()

i=0
"""
for i in range(20):
    mc.setBlock(x,y-1,z+i,73)
"""
for i in range(20):
    mc.setBlocks(x+i,y-1,z+i,x+i,y-1,z+2+i,73)