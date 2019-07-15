# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        arr=[1]
        p2=0
        p3=0
        p5=0
        i=0
        while(i<index):
            res=min(arr[p2]*2,arr[p3]*3,arr[p5]*5)
            arr.append(res)
            if res ==arr[p2]*2: p2+=1
            if res ==arr[p3]*3: p3+=1
            if res ==arr[p5]*5: p5+=1
            i+=1
        return arr[-1]