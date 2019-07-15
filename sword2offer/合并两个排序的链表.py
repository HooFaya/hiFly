# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # 返回合并后列表

    """
    思路：需要三个工作指针
    分别服务新链表和两个原链表
    第一步，先确定头节点的位置
    第二步，找新节点
    具体看下面的代码注释
    """
    def Merge(self, pHead1, pHead2):
        """考虑特殊情况，常规且必须"""
        if pHead1 is None:
            return pHead2
        if pHead2 is None:
            return pHead1

        cur1 = pHead1
        cur2 = pHead2
        new_head = None
        cur = None
        if cur1.val < cur2.val:
            new_head = cur1
            cur = cur1
            cur1 = cur1.next
        else:
            new_head = cur2
            cur = cur2
            cur2 = cur2.next
        while (cur1 and cur2):
            if cur1.val < cur2.val:
                cur.next = cur1
                # 第一遍做的时候忘记移动cur，也就是少写了下面的cur=cur1
                cur = cur1
                cur1 = cur1.next
            else:
                cur.next = cur2
                # 第一遍做的时候忘记移动cur，也就是少写了下面的cur=cur2
                cur = cur2
                cur2 = cur2.next
        """
        将剩余节点加入套餐
        """
        if cur1 is not None:
            cur.next = cur1
        if cur2 is not None:
            cur.next = cur2
        return new_head

        # write code here