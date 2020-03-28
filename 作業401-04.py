# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 16:33:52 2020

@author: p35k
"""

import time
from mcpi.minecraft import Minecraft
mc=Minecraft.create()

while True:
        x,y,z=mc.player.getTilePos()
        mc.setBlock(x, y, z, 8)
        time.sleep(30)