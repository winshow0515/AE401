# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 10:57:20 2020

@author: p35k
"""
import time
from mcpi.minecraft import Minecraft
mc=Minecraft.create()

while True:
    x,y,z=mc.player.getTilePos()
    mc.postToChat("x="+str(x)+" y="+str(y)+" z="+str(z))
    time.sleep(0.5)