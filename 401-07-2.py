# -*- coding: utf-8 -*-
"""
Created on Sat Apr 25 12:07:44 2020

@author: p35k
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x,y,z=mc.player.getTilePos()

mc.setBlocks(x,y+3,z+1,x+2,y+5,z-1,18,0)
mc.setBlocks(x+1,y,z,x+1,y+4,z,17,0)