# -*- coding: utf-8 -*-
"""
Created on Wed May 13 17:02:51 2020

@author: p35k
"""
from mcpi.minecraft import Minecraft
mc=Minecraft.create()

def buildPyramid3(x,y,z,base):
    #高
    height=(base//2)+1
    
    for i in range(height):
        x1=x + i
        y1=y + i
        z1=z + i
        
        x2=x+base-i
        z2=z+base-i
        mc.setBlocks(x1,y1,z1,x2,y1,z2,24)
        mc.setBlocks(x1+1,y1,z1+1,x2-1,y1,z2-1,0)
    mc.setBlock(x1,y1,z1,24)

x,y,z=mc.player.getTilePos()
buildPyramid3(x,y,z,10)