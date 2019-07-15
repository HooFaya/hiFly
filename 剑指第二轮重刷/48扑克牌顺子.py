# -*- coding:utf-8 -*-
class Solution:
    def IsContinuous(self, numbers):
        if not numbers:
            return False
        numbers.sort()
        nums=[item for item in numbers if item != 0]
        key=len(numbers)-len(nums)
        diff=0
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                return False
            diff+=nums[i]-nums[i-1]-1
        return key>=diff