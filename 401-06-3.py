# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 11:30:15 2020

@author: p35k
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
import random
import time

pos=mc.player.getPos()

while True:
    x=pos.x #+random.uniform(-1,1)
    z=pos.z #+random.uniform(-1,1)
    y=pos.y + 5
    print('x=' + str(x))  
    mc.spawnEntity(x, y, z, 93)
    time.sleep(0.5)