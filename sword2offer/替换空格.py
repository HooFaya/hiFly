# -*- coding:utf-8 -*-
# 请实现一个函数，将一个字符串中的每个空格替换成“%20”。
# 例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy


class Solution:
    # 此题用python字符串的replace函数很容易解决
    # 第二种方法如下，将字符串转换成列表，依次遍历，替换空格
    def replaceSpace(self, s):
        str_list = list(s)
        for index, item in enumerate(s):
            if item == " ":
                str_list[index] = "%20"
        return "".join(str_list)

