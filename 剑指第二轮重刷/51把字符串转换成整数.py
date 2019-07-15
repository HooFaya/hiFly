# -*- coding:utf-8 -*-
class Solution:
    def StrToInt(self, s):
        if not s:
            return 0
        index,flag=0,0
        if s[0]=="+" or s[0]=="-":
            index=1
        else:
            index=0
        if s[0]=="-":
            flag=-1
        else:
            flag=1
        res=""
        for i in range(index,len(s)):
            if ord(s[i])<ord("0") or ord(s[i])>ord("9"):
                return 0
            else:
                res+=s[i]
        if not res:
            return 0
        return flag*int(res)
s=Solution()
print(s.StrToInt("das12332"))

