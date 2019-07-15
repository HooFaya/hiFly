#输入一个链表，输出该链表中倒数第k个结点
# -*- coding:utf-8 -*-


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    """
    快慢指针法

    注意判断特殊情况，当心节点总数小于k，可以与面试官沟通此时应该返回什么

    """
    def FindKthToTail(self, head, k):
        if head is None or k < 0:
            return
        fast = head
        slow = head
        c = 0
        while (fast and c < k):
            fast = fast.next
            c += 1
        if c < k:
            return

        while (fast):
            slow = slow.next
            fast = fast.next
        return slow

        # write code here