"""
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
输入一个数组,求出这个数组中的逆序对的总数P。
并将P对1000000007取模的结果输出。 即输出P%1000000007
"""
# -*- coding:utf-8 -*-
# -*- coding:utf-8 -*-
""" 冒泡超时，记得要交换，不然不是逆序对的数目"""
class Solution_1:
    def InversePairs(self, data):
        c=0
        for i in range(len(data)):
            for j in range(len(data)-1-i):
                if data[j]>data[j+1]:
                    data[j],data[j+1]=data[j+1],data[j]
                    c=+1
        # write code here
        return c%1000000007

# -*- coding:utf-8 -*-
"""归并思路"""
class Solution_2:
    def __init__(self):
        self.count=0

    def InversePairs(self,data):
        self.InversePairs_helper(data)
        return self.count

    def InversePairs_helper(self, data):
        if len(data)==1:
            return data
        mid=len(data)//2
        left=self.InversePairs_helper(data[:mid])
        right=self.InversePairs_helper(data[mid:])
        return self.merge_count(left,right)

    def merge_count(self,left,right):
        if not left:
            return right
        if not right:
            return left
        i,j=0,0
        res=[]
        while(i<len(left) and j<len(right)):
            if left[i]<right[j]:
                res.append(left[i])
                i+=1
            else:
                self.count+=len(left[i:])
                res.append(right[j])
                j+=1
        res.extend(left[i:])
        res.extend(right[j:])
        return res
s=Solution_2()
print(s.InversePairs([1,2,3,4,5,6,7,0]))





