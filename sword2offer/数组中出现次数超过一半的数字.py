"""哈希法"""
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        dic={}
        for item in numbers:
            dic[item]=dic.setdefault(item,0)+1
        for k,v in dic.items():
            if v>len(numbers)//2:
                return k
        return

"""扫描法"""
class Solution_2:
    def MoreThanHalfNum_Solution(self, numbers):
        init=numbers[0]
        count=0
        for item in numbers:
            if item==init:
                count+=1
            else:
                count-=1
            if count==0:
                init=item
                count=1
        count=0
        for item in numbers:
            if item==init:
                count+=1
        if count>len(numbers)//2:
            return init
        return 0

s=Solution_2()
print(s.MoreThanHalfNum_Solution([1,2,3,2,2,2,5,4,2]))

