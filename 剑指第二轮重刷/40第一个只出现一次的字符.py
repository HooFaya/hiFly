# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        dic={}
        for item in s:
            dic[item]=dic.setdefault(item,0)+1
        l=[]
        for k,v in dic.items():
            if v==1:
                l.append(k)
        for item in s:
            if item in l:
                return item