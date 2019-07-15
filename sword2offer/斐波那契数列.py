# 大家都知道斐波那契数列，
# 现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。
# n<=39

# -*- coding:utf-8 -*-
"""easy,无Fuck说"""
"""注意看要求，从0开始，如果从1开始就返回b"""
class Solution:
    def Fibonacci(self, n):
        a,b=0,1
        t=0
        while(t<n):
            a,b=b,a+b
            t+=1
        return a
