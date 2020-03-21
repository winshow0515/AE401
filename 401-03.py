# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 10:20:04 2020

@author: p35k
"""

from mcpi.minecraft import Minecraft
#連結 mcpi 資料夾
mc=Minecraft.create()
#連結Minecraft

x,y,z=mc.player.getTilePos()
#西瓜
mc.setBlock(x, y-1, z, 103) 
#烽火台
mc.setBlock(x+1, y-1, z, 138)
#白色界伏盒
mc.setBlock(x+1, y-1,z-1, 219)
#灰壤
mc.setBlock(x, y-1, z-1, 3,2)
#音階盒
mc.setBlock(x-1, y-1, z, 25)
#基岩
mc.setBlock(x-1, y-1, z, 7)
#鵝卵石
mc.setBlock(x-1, y-1, z+1, 4)
#海綿
mc.setBlock(x, y-1, z+1, 19,0)
#青金石礦
mc.setBlock(x+1, y-1, z+1, 21)
#金礦
mc.setBlock(x-1, y-1, z-1, 41)
#羊毛
#mc.setBlock(x-10, y, z, 35,0)