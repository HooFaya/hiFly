"""
把只包含质因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，
因为它包含质因子7。 习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
"""
# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        if index<=0:
            return 0
        p2,p3,p5=0,0,0
        arr=[1]
        i=0
        while(i<index):
            res=min(arr[p2]*2,arr[p3]*3,arr[p5]*5)
            arr.append(res)
            if res==arr[p2]*2:p2+=1
            if res==arr[p3]*3:p3+=1
            if res==arr[p5]*5:p5+=1
            i+=1
        return arr[index-1]

