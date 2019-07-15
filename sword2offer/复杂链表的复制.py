"""
输入一个复杂链表
（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针指向任意一个节点），
返回结果为复制后复杂链表的head。（
注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）
"""
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
class Solution:
    def Clone(self,pHead):
        cur=pHead
        while(cur):
            new=RandomListNode(cur.label)
            tmp=cur.next
            cur.next=new
            new.next=tmp
            cur=tmp
        cur=pHead
        """注意循环结束条件，如果换成cur.next则出现None.next的情况，这是会报错的"""
        while(cur):
            if cur.random:
                cur.next.random=cur.random.next
            else:
                cur.next.random=None
            cur=cur.next.next
        res=pHead.next
        cur=pHead
        while(cur.next):
            tmp=cur.next
            cur.next=cur.next.next
            cur=tmp
        return res

