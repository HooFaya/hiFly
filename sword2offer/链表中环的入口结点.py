# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 此题的思路很明朗，利用快慢指针先找到相遇节点，
    # 再利用等速指针同时从相遇点和起始点出发找到入口点
    # 实际编程中要注意移动指针和判断退出这两步的先后顺序
    # 在找到相遇点时要先移动再判断，这是因为如果先判断，那么循环一开始，slow和fast肯定相等，循环直接退出
    # 在找入口时要先判断再移动，这是因为如果先移动，如果头节点就是入口节点就会导致，出口节点被误判为下一个节点
    def EntryNodeOfLoop(self, pHead):
        if pHead is None or pHead.next is None:
            return None

        # write code here
        def find_meet(pHead):
            slow = pHead
            fast = pHead
            while (fast and fast.next):
                fast = fast.next.next
                slow = slow.next
                if fast is slow:
                    return slow

            return None

        def find_enter(meet, pHead):
            while (True):
                if meet is pHead:
                    return meet
                pHead = pHead.next
                meet = meet.next

        if find_meet(pHead):
            meet = find_meet(pHead)
            enter = find_enter(meet, pHead)
            return enter
        else:
            return None


