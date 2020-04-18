# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 11:13:46 2020

@author: p35k
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x,y,z=mc.player.getTilePos()
mc.setSign(x,y,z,63,5,["","!!!$$$!!!","^^",""])