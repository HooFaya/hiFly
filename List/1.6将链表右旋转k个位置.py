"""
快慢指针法
"""
import aux
class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None
"""
函数功能：向右旋转k个单位
"""
def lreversek(head,k):
    if head is None or head.next is None:
        return head
    fast=head.next
    slow=head.next
    count=0
    while(count<k and fast):
        fast=fast.next
        count+=1
    if count<k:
        return None
    while(fast.next):
        fast=fast.next
        slow=slow.next
    tmp=head.next
    head.next=slow.next
    fast.next=tmp
    slow.next=None






if __name__ =="__main__":
    head=aux.constructList()
    aux.printList(head)
    lreversek(head,3)
    print("\n")
    aux.printList(head)





