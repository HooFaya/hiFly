# -*- coding:utf-8 -*-
# 用两个栈来实现一个队列，完成队列的Push和Pop操作。
# 队列中的元素为int类型。


class Solution:
    # 一个栈用来存放入栈
    # 另一个栈用于出栈，出栈的时候先判断本栈是否为空，如果为空，将第一个栈的数出栈到本栈
    def __init__(self):
        self.stack1=[]
        self.stack2=[]
    def push(self, node):
        self.stack1.append(node)
        # write code here
    def pop(self):
        if len(self.stack2)==0:
            while( len(self.stack1)!=0):
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()
