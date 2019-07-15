import aux
"""
      要求：
对链表进行重新排序，例如
1>>2>>3>>...>>n
排序为
1>>n>>2>>n-1>>...
      方法：
利用快慢指针，将链表拆分成两段，然后将后半段逆序，然后前后两段进行拼接
"""
class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None


'''

 方法功能：找到列表的中间节点并断开列表
 输入参数：链表的头节点
 返回值：链表的中间节点，同时也是后半截节点的首节点
 
'''
def findMiddleNode(head):
    if head is None or head.next is None:
        return head
    slow=head
    fast=head
    slowPre=head
    while(fast and fast.next):
        fast=fast.next.next
        slowPre=slow
        slow=slow.next
    slowPre.next=None
    return slow


'''
方法功能：对不带头节点的链表进行逆序
输入参数：链表的首节点
返回值：逆序后链表的首节点
'''
def reverse(head):
    if head is None or head.next is None:
        return head
    pre=None
    cur=head
    while(cur):
        next=cur.next
        cur.next=pre
        pre=cur
        cur=next
    return pre


"""
函数功能：重新排序
输出参数：链表的首节点
返回值：无
"""
def reorder(head):
    cur1=head.next
    mid=findMiddleNode(head)
    cur2=reverse(mid)
    while(cur1.next):
        tmp=cur1.next
        cur1.next=cur2
        cur1=tmp
        tmp=cur2.next
        cur2.next=cur1
        cur2=tmp
    cur1.next=cur2


if __name__ =="__main__":
    head=aux.constructList()
    # aux.printList(head)
    # mid=findMiddleNode(head)
    #
    # print("\n前半段列表:")
    # aux.printList(head)
    # print("\n后半段列表:")
    # cur=mid
    # while(cur):
    #     print(cur.data,end=" ")
    #     cur=cur.next
    # print("\n后半段反转之后的列表：")
    # cur=reverse(mid)
    # while(cur):
    #     print(cur.data,end=" ")
    #     cur=cur.next
    # print("\n")
    reorder(head)
    aux.printList(head)


















