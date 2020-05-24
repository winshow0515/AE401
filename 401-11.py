# -*- coding: utf-8 -*-
"""
Created on Sat May 23 10:00:32 2020

@author: p35k
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
from random import randrange


for i in range(10):
    x,y,z=mc.player.getTilePos()
    x=x+i
    
    for j in range(10):
        r=randrange(0,16)
        z=z+1
        mc.setBlock(x,y,z,35,r)