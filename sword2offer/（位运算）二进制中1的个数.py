# -*- coding:utf-8 -*-
class Solution:
    """
    此题思路明朗，111&110=110，110&101=100
    值得注意的是
    python的int类型是无线精度的,所以截取32位即可,
    截取之后即为正常的补码表示
    """
    def NumberOf1(self, n):
        count = 0
        n = n & 0xffffffff
        while (n):
            n = n & (n - 1)
            count += 1
        return count
        # write code here
s=Solution()
print(s.NumberOf1(-7))
