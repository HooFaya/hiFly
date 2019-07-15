class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def Merge(self, pHead1, pHead2):
        if not pHead1:
            return pHead2
        if not  pHead2:
            return pHead1
        head=None
        cur=None
        cur1=pHead1
        cur2=pHead2
        if cur1.val < cur2.val:
            head =cur1
            cur=cur1
            cur1=cur1.next
        else:
            head=pHead2
            cur=pHead2
            cur2=pHead2.next
        while(cur1 and cur2):
            if cur1.val<cur2.val:
                cur.next=cur1
                cur1=cur1.next
                cur=cur.next
            else:
                cur.next=cur2
                cur2=cur2.next
                cur=cur.next
        if not cur1:
            cur.next=cur2
        if not cur2:
            cur.next=cur1
        return head


