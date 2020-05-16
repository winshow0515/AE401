# -*- coding: utf-8 -*-
"""
Created on Sat May 16 11:04:24 2020

@author: p35k
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
from time import sleep
while True:
    mc.executeCommand("time add 50")
    sleep(0.05)