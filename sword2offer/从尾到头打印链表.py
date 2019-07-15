# -*- coding:utf-8 -*-

# 输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution_1:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    # 现顺序遍历再利用列表的reverse方法
    def printListFromTailToHead(self, listNode):
        lis = []
        while (listNode is not None):
            lis.append(listNode.val)
            listNode = listNode.next
        return list(reversed(lis))


class Solution_2:
    # 递归解法
    def __init__(self):
        self.res = []

    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        self.printListFromTailToHead_helper(listNode)
        return self.res

    def printListFromTailToHead_helper(self, listNode):
        if not listNode:
            return
        self.printListFromTailToHead(listNode.next)
        self.res.append(listNode.val)