
#Created on Sat Apr 11 11:21:27 2020

#@author: p35k


from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x,y,z=mc.player.getTilePos()
try:
    blockType = int(input("請輸入要放的方塊ID:"))
    mc.postToChat("blockType="+str(blockType))
    x1 = int(input("請輸入x1:"))
    mc.postToChat("x1="+str(blockType))
    y1 = int(input("請輸入y1:"))
    mc.postToChat("y1="+str(blockType))
    z1 = int(input("請輸入z1:"))
    mc.postToChat("z1="+str(blockType))

except:
    print("只能輸入數字")

mc.setBlocks(x-x1, y-y1, z-z1, x+x1, y+y1, z+z1 , blockType)
mc.setBlocks(x-x1+1, y-y1+1, z-z1+1, x+x1-1, y+y1-1, z+z1-1, 0)
mc.setBlocks(x-x1, y+y1, z-z1, x+x1, y+y1, z+z1, 169)
mc.setBlock(x+x1, y, z, 0)