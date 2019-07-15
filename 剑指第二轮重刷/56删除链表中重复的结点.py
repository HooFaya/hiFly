"""
题目描述
在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留，返回链表头指针。
例如，链表1->2->3->3->4->4->5 处理后为 1->2->5
"""

# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        head=ListNode("#")
        head.next=pHead
        pre=head
        cur=head.next
        while(cur and cur.next):
            if cur.val ==cur.next.val:
                while(cur and cur.val==cur.next.val):
                    cur=cur.next
                pre.next=cur.next
                cur=cur.next
            else:
                cur=cur.next
                pre=pre.next

        return head.next
l1=ListNode(1)
l2=ListNode(1)
l3=ListNode(1)
l4=ListNode(1)
l1.next=l2
l2.next=l3
l3.next=l4
cur=l1
while(cur):
    print(cur.val,end=" ")
    cur=cur.next
s=Solution()
s.deleteDuplication(l1)
cur=l1
print("\n")
while(cur):
    print(cur.val,end=" ")
    cur=cur.next
