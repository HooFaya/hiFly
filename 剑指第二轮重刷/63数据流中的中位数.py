# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.data=[]
    def Insert(self, num):
        self.data.append(num)
        self.data.sort()

    def GetMedian(self,data=None):
        if len(self.data)%2==1:
            return self.data[len(self.data)//2]
        else:
            first=self.data[len(self.data)//2-1]
            second=self.data[len(self.data)//2]
            return (first+second)/2.0
