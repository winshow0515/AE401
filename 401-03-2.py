# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 11:33:26 2020

@author: p35k
"""

from mcpi.minecraft import Minecraft
#連結 mcpi 資料夾
mc=Minecraft.create()
#連結Minecraft
x,y,z=mc.player.getTilePos()
mc.setBlocks(x-2, y-1, z, x+2, y-1, z, 152)
mc.setBlocks(x-1, y-1, z+1, x+1, y-1, z+1, 152)
mc.setBlock(x, y-1, z+2, 152)
