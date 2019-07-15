# -*- coding:utf-8 -*-
"""
题目描述
请实现一个函数用来找出字符流中第一个只出现一次的字符。
例如，当从字符流中只读出前两个字符"go"时，
第一个只出现一次的字符是"g"。当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。
"""
class Solution:
    def __init__(self):
        self.dic={}
    def FirstAppearingOnce(self):
        for k,v in self.dic.items():
            if v==1:
                return k
        return "#"

    def Insert(self, char):
        self.dic[char]=self.dic.setdefault(char,0)+1

s=Solution()
s.Insert('g')
s.Insert("o")
print(s.FirstAppearingOnce())
s.Insert("o")
s.Insert("g")
print(s.FirstAppearingOnce())

s.Insert("l")
s.Insert("e")
print(s.FirstAppearingOnce())
