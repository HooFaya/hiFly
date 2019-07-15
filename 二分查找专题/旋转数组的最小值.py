# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        if not rotateArray:
            return 0
        l=0
        r=len(rotateArray)-1
        while(rotateArray[l]>=rotateArray[r]):
            if r-l==1:
                return rotateArray[r]
            m=l+(r-l)//2
            if rotateArray[l]==rotateArray[m] and rotateArray[r]==rotateArray[m]:
                return min(rotateArray)
            if rotateArray[m]>rotateArray[r]:
                l=m
            else:
                r=m
        return rotateArray[m]

