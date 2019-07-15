# -*- coding:utf-8 -*-

"""
思路：
利用两个栈，一个栈用于存放元素一个栈用于存放元素的最小值

在弹出时，判断要弹出的元素是否等于最小元素，如果是，就一起弹出
在压入时，判断要压入的元素是否小于最小元素，如果小于，就将此元素同时压入两个栈中

"""
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        self.stack2.append(2 ** 31)

    def push(self, node):
        if node < self.stack2[len(self.stack2) - 1]:
            self.stack2.append(node)
        self.stack1.append(node)

        # write code here

    def pop(self):
        if self.stack1[len(self.stack1) - 1] == self.stack2[len(self.stack2) - 1]:
            self.stack2.pop()
        return self.stack1.pop()

        # write code here

    def top(self):
        return self.stack1[len(self.stack1) - 1]
        # write code here

    def min(self):
        return self.stack2[len(self.stack2) - 1]
        # write code here