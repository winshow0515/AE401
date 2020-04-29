# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 21:12:06 2020

@author: p35k
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x,y,z=mc.player.getTilePos()

#建星光大道
mc.setBlocks(x-20,y-1,z-1,x+20,y-1,z+1,4)
mc.setBlocks(x-1,y-1,z-20,x+1,y-1,z+20,4)

#建房子
mc.setBlocks(x+3,y-1,z+3,x-3,y+3,z-3,35,4)
mc.setBlocks(x+2,y,z+2,x-2,y+2,z-2,0)
mc.setBlocks(x+3,y,z,x-3,y+1,z,0)
mc.setBlocks(x,y,z+3,x,y+1,z-3,0)
mc.setBlock(x,y,z,50)