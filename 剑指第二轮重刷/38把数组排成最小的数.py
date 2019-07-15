# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self, numbers):
        for i in range(1, len(numbers)):
            j = i
            while (j>0):
                if self.will_change(numbers[j - 1], numbers[j]):
                    numbers[j - 1], numbers[j] = numbers[j], numbers[j - 1]
                j -= 1
        numbers=map(str,numbers)
        return "".join(numbers)

    def will_change(self, s1, s2):
        x1 = int(str(s1) + str(s2))
        x2 = int(str(s2) + str(s1))
        return x2 < x1

s=Solution()
print(s.PrintMinNumber([3,5,1,4,2]))