# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 10:00:00 2020

@author: p35k
"""

from mcpi.minecraft import Minecraft
#連結 mcpi 資料夾
mc=Minecraft.create()
#連結Minecraft
x,y,z=mc.player.getTilePos()

mc.setBlocks(x-1, y-1, z-1, x+1, y+2, z+1, 95,0)
mc.setBlocks(x, y, z, x, y+1, z, 0)