# -*- coding:utf-8 -*-
# 题目描述：
# 在一个二维数组中（每个一维数组的长度相同
# 每一行都按照从左到右递增的顺序排序，
# 每一列都按照从上到下递增的顺序排序。
# 请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。


class Solution:
    # array 二维列表
    # 此题的思路很简单，就是利用二维数组的有序性，从数组的左下角开始搜索
    #  此题需要注意的是循环退出的边界，行标肯定可以等于零，列标小于列数
    #  即i >= 0 and j < col_length
    def Find(self, target, array):
        # write code here
        row_length = len(array)
        col_length = len(array[0])
        i = row_length - 1
        j = 0
        while i >= 0 and j < col_length:
            if target < array[i][j]:
                i -= 1
            elif target > array[i][j]:
                j += 1
            else:
                return True
        return False
