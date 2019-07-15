# -*- coding:utf-8 -*-
class Solution:
    def InversePairs(self, data):
        self.count=0
        self.merge_sort(data)
        return self.count
    def merge_sort(self,data):
        if len(data)==1:
            return data
        mid=len(data)//2
        left=self.merge_sort(data[:mid])
        right=self.merge_sort(data[mid:])
        return self.merge(left,right)
    def merge(self,left,right):
        if not left:
            return right
        if not right:
            return  left
        i,j=0,0
        res=[]
        while(i<len(left) and j<len(right)):
            if left[i]<right[j]:
                res.append(left[i])
                i+=1
            else:
                res.append(right[j])
                self.count+=len(left[i:])
                j+=1
        res.extend(left[i:])
        res.extend(right[j:])
        return res


s=Solution()

print(s.InversePairs([1,2,3,4,5,6,7,0]))