# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        if not pHead2 or not pHead1:
            return
        cur=pHead1
        stack1=[]
        while(cur):
            stack1.append(cur)
            cur=cur.next

        cur=pHead2
        stack2=[]
        while(cur):
            stack2.append(cur)

        while(stack2 and stack2 and stack1[-1] is stack2[-1]):
            cur=stack1.pop()
            stack2.pop()
        return cur

