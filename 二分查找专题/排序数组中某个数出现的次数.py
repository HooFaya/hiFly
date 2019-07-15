# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        if not data :
            return
        first=self.get_first_k(data,k)
        last=self.get_last_k(data,k)
        return last-first+1
    def get_first_k(self,data,k):
        l=0
        r=len(data)-1
        while(l<=r):
            m=l+(r-l)//2
            if data[m]==k:
                while(m-1>=0 and data[m]==data[m-1]):
                    m-=1
                return m
            elif k<data[m]:
                r=m-1
            else:
                l=m+1
        return -1
    def get_last_k(self,data,k):
        l=0
        r=len(data)-1
        length=len(data)
        while(l<=r):
            m=l+(r-l)//2
            if data[m]==k:
                while(m+1<length and data[m+1]==data[m]):
                    m+=1
                return m
            elif k<data[m]:
                r=m-1
            else:
                l=m+1
        return -1
