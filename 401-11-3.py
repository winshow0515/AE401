# -*- coding: utf-8 -*-
"""
Created on Sat May 23 11:22:46 2020

@author: p35k
"""
from time import time,sleep

def LinearSearch(ans):
    sTime=time()
    for i in range(100000000):
        if ans == i:
            print("答案是"+str(i))
            print("花了"+str(time()-sTime)+"秒")
            break
        

def BinarySearch(r):
    sTime=time()
    low=0
    upper=100000000
    
    while low <= upper:
        mid=(low+upper)//2
        
        if mid < r:
            low=mid+1
        
        elif mid > r:
            upper = mid-1
        
        else:
            print("答案是"+str(mid))
            print("二元搜尋法:花了"+str(time()-sTime)+"秒")
            return


#LinearSearch(10000000)
BinarySearch(100000000)      