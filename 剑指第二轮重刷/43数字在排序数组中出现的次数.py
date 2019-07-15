# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        start=self.get_first(data,k)
        end=self.get_last(data,k)
        if start==-1:
            return
        return end-start+1

    def get_first(self,data,k):
        l=0
        r=len(data)-1
        while(l<=r):
            m=l+(r-l)//2
            if k<data[m]:
                r=m-1
            elif data[m]<k:
                l=m+1
            else:
                while(m-1>=0 and data[m]==data[m-1]):
                    m-=1
                return m
        return -1
    def get_last(self,data,k):
        l=0
        r=len(data)-1
        while(l<=r):
            m=l+(r-l)//2
            if k<data[m]:
                r=m-1
            elif data[m]<k:
                l=m+1
            else:
                while(m+1<len(data) and data[m+1]==data[m]):
                    m+=1
                return m
        return -1

s=Solution()
print(s.get_last([1,3,3,3,3,4,5],2))
print(s.get_first([1,3,3,3,3,4,5],2))
