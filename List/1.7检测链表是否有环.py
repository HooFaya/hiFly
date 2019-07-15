import aux
'''
方法：快慢节点
'''
def isLoop(head):
    if head is None or head.next is None:
        return head
    slow=head.next
    fast=head.next
    while(fast and fast.next):
        slow=slow.next
        fast=fast.next.next
        if slow is fast:
            return slow

    return None
def findLoopNode(head):
    p1=head.next
    p2=isLoop(head)
    while p1 is not p2:
        p1=p1.next
        p2=p2.next
    return p1


