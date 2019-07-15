# 把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
# 输入一个非减排序的数组的一个旋转，输出旋转数组的最小元素。
# 例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
# NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。

# -*- coding:utf-8 -*-
"""
看到非减序列，输出最小元素（即在一个有序序列里查找一个数），首先应该想到二分查找
此题正是二分查找的变体
旋转数组的意思就是把原来的非递减数组拆解成两个非递减数组
旋转的意思就是前面一个非递减数组的最小值不小于后面一个非递减数组的最大值
具体解析参考下面的代码注释

"""


class Solution:
    def minNumberInRotateArray(self, rotateArray):
        """判断特殊情况，数组为空，返回0"""
        if len(rotateArray) == 0:
            return 0
        left = 0
        right = len(rotateArray) - 1
        """判断特殊情况，如果数组不是旋转数组"""
        if rotateArray[left] < rotateArray[right]:
            return rotateArray[0]
        """while循环保证数组的旋转性"""
        while (rotateArray[left] >= rotateArray[right]):
            """left永远在前面一个非递减序列中，right永远在后面一个非递减序列中"""
            """所以循环的退出条件很重要，就是下面这句"""
            if (right - left) == 1:
                return rotateArray[right]

            mid = (right + left + 1) // 2
            """判断特殊情况，[1,1,1,1,1,1]"""
            if rotateArray[mid] == rotateArray[right] and rotateArray[right] == rotateArray[left]:
                return min(rotateArray)
            """当中间的数大于left指向的数，说明mid还在前面的非递减序列中"""
            if rotateArray[mid] >= rotateArray[left]:
                left = mid
            if rotateArray[mid] < rotateArray[left]:
                right = mid
        return rotateArray[mid]



s=Solution()
print(s.minNumberInRotateArray([3,4,5,1,2]))