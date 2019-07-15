# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self,val):
        self.val=val
        self.next=None
class Solution:
    def LastRemaining_Solution(self, n, m):
        head=self.construct_list(n)
        cur=head
        while(n!=1):
            for i in range(m-2):
                cur=cur.next
            cur.next=cur.next.next
            cur=cur.next
            n-=1
        return cur.val
    def construct_list(self,n):
        head=ListNode(0)
        cur=head
        for i in range(1,n):
            cur.next=ListNode(i)
        cur.next=head



