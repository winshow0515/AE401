# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 11:23:50 2020

@author: p35k
"""

import time
from mcpi.minecraft import Minecraft
mc=Minecraft.create()
m = 1
x,y,z=mc.player.getTilePos()
while m < 20:
    mc.setBlocks(x+10, y-5, z, x-10, y+5, z, 19)
    z=z+5
    m = m+1
    time.sleep(0.2)