import aux
"""
快慢指针法
"""
class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None
"""
函数功能：返回链表倒数第K个节点
输入参数：头节点，K
"""
def findLastkValue(head,k):
    if head is None or head.next is None:
        return head
    fast=head.next
    slow=head.next
    count=0
    while(count<k and fast):
        fast= fast.next
        count+=1
    if count<k:
        return None
    while(fast):
        fast=fast.next
        slow=slow.next
    return slow
if __name__== "__main__":
    head=aux.constructList()
    aux.printList(head)
    result=findLastkValue(head,3)
    print('\n',result.data)


