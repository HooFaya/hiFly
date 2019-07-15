#一只青蛙一次可以跳上1级台阶，也可以跳上2级。
#求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）

# -*- coding:utf-8 -*-
"""此题看似简单的斐波那契数列，但是有些细节需要注意"""

class Solution:
    def jumpFloor(self, number):
        a,b=1,2
        """和传统的斐波那契不一样的是，循环起始值是n=1"""
        n=1
        while(n<number):
            a,b=b,a+b
            n=n+1
        return a

        # write code here