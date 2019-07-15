"""
在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,
并返回它的位置, 如果没有则返回 -1（需要区分大小写）.
"""


class Solution:
    def FirstNotRepeatingChar(self, s):
        ss = list(s)
        dic = {}
        res = []
        for item in ss:
            dic[item] = dic.setdefault(item, 0) + 1
        for k, v in dic.items():
            if v == 1:
                res.append(k)
        if not res:
            return -1
        for index, item in enumerate(ss):
            if item in res:
                return index

        # write code here