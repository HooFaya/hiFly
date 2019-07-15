# -*- coding:utf-8 -*-
class Solution:
    def Add(self, num1, num2):
        while(num2!=0):
            s=(num1^num2) & 0xffffffff
            c=((num1&num2)<<1) & 0xffffffff
            num1=s
            num2=c
        return num1 if num1<0x7fffffff else ~(num1 ^ 0xffffffff)

