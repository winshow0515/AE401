# -*- coding: utf-8 -*-
"""
Created on Sat May  9 10:27:58 2020

@author: p35k
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()

pos=mc.player.getTilePos()

def buildPyramid1(x,y,z):
    #寬
    base=10
    #高
    height=(base//2)+1
    
    for i in range(height):
        x1=pos.x + i
        y1=pos.y + i
        z1=pos.z + i
        
        x2=x1+base-i
        z2=z1+base-i
        mc.setBlocks(x1,y1,z1,x2,y1,z2,35,4)


def buildPyramid2(x,y,z,base):
    #高
    height=(base//2)+1
    
    for i in range(height):
        x1=x + i
        y1=y + i
        z1=z + i
        
        x2=x+base-i
        z2=z+base-i
        mc.setBlocks(x1,y1,z1,x2,y1,z2,35,4)

x,y,z=mc.player.getTilePos()
buildPyramid2(x,y,z,10)