# 一只青蛙一次可以跳上1级台阶，也可以跳上2级……
# 它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法

# -*- coding:utf-8 -*-

"""
小青蛙跳的时候面临两种选择，
第一，跳到终点，游戏结束
第二，跳到非终点的任意一个位置，游戏继续
这样的选择可以选n-1次，这是因为到了倒数第二个台阶，倒数第一是他唯一的选择
蛙生啊，除了最后的走投无路都是有选择的余地，exciting!
"""
class Solution:
    def jumpFloorII(self, number):
        return 2**(number-1)
        # write code here