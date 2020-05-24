# -*- coding: utf-8 -*-
"""
Created on Sat May 23 10:45:18 2020

@author: p35k
"""
from mcpi.minecraft import Minecraft
mc=Minecraft.create()
from random import randrange

r=randrange(1,16)

while True:
    hits = mc.events.pollBlockHits()
    if len(hits)>0:
    
        hit=hits[0]
        
        Block=mc.getBlockWithData(hit.pos)
        data=Block.data
    
        if data == r:
            mc.postToChat("恭喜!答對了!答案是"+str(r))
            mc.setBlock(hit.pos,57)
            break
        elif data<r:
            mc.postToChat("太小了!")
            
        elif data>r:
            mc.postToChat("太大了!")
                
