# -*- coding: utf-8 -*-
"""
Created on Sat May  2 10:05:50 2020

@author: p35k
"""
#    plantTree(x+i,y,z)
#for i in range(0,25,5):

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x,y,z=mc.player.getTilePos()

def plantTree(x,y,z):
    mc.setBlocks(x-1,y+3,z+2,x+3,y+5,z-2,18,0)
    mc.setBlocks(x,y+6,z-1,x+2,y+6,z+1,18,0)
    mc.setBlocks(x+1,y,z,x+1,y+5,z,17,0)
'''
for i in range(5):
    plantTree(x+i*5,y,z)
    plantTree(x-i*5,y,z)
    plantTree(x,y,z+i*5)
    plantTree(x,y,z-i*5)
'''
o=-1
for i in range(5):
    o=o+5
    for j in range(5):
        for p in range(5):
            plantTree(x+i*o,y+p*o,z+j*o)
            
