# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        if not pHead:
            return
        meet=self.find_meet(pHead)
        if meet:
            return self.find_res(pHead,meet)


    def find_meet(self,pHead):
        fast=pHead
        slow=pHead
        while(fast and fast.next):
            fast=fast.next.next
            slow=slow.next
            if fast is slow:
                return slow
    def find_res(self,pHead,meet):
        p1=pHead
        p2=meet
        while(True):
            if p1 is p2:
                return p1
            p1=p1.next
            p2=p2.next

n1=ListNode(1)
n2=ListNode(2)
n3=ListNode(3)
n4=ListNode(4)

n1.next=n2
n2.next=n3
n3.next=n4
n4.next=n2

s=Solution()
print(s.EntryNodeOfLoop(n1).val)