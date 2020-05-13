# -*- coding: utf-8 -*-
"""
Created on Sat May  9 11:23:51 2020

@author: p35k
"""
from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x,y,z=mc.player.getTilePos()

line1=[]
for i in range(1,4):
    line1.append(1*i)

line2=[]
for i in range(1,4):
    line2.append(2*i)

line3=[]
for i in range(1,4):
    line3.append(3*i)


mc.setSign(x,y,z,63,5,[str(line1),str(line2),str(line3),""])