# -*- coding:utf-8 -*-
"""注意n=1"""
class Solution:
    def rectCover(self, number):
        if number==0:
            return 0
        a,b=1,2
        n=1
        while(n<number):
            a,b=b,a+b
            n+=1
        return a