# -*- coding:utf-8 -*-
class Solution:
    def FindContinuousSequence(self, tsum):
        if tsum==0:
            return []
        if tsum==1:
            return 1
        nums=list(range(1,tsum+1))
        l=0
        r=1
        res=[]
        while(l<r):
            s=(r-l+1)*(nums[l]+nums[r])/2
            if s>tsum:
                l+=1
            elif s<tsum:
                r+=1
            else:
                res.append(s[l:r+1])
                l+=1

        return res


