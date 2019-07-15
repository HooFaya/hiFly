# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        array.sort()
        l=0
        r=len(array)-1
        while(l<r):
            if array[l]+array[r]==tsum:
                return [array[l],array[r]]
            elif array[l]+array[r] <tsum:
                l+=1
            else:
                r-=1