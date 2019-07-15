import  aux

# def reverse(head):
#     if head is None:
#         return head
#     pre=None
#     cur=head
#     while(cur):
#         next=cur.next
#         cur.next=pre
#         pre=cur
#         cur=next
#     return pre
# def reverseK(head,k):
#     if head is None or head.next is None or k<2:
#         return
#     pre=head
#     cur1=head.next
#     i=1
#     while(cur1):
#         cur2=cur1
#         while(i<k):
#             if cur2.next is not None:
#                 cur2=cur2.next
#             else:
#                 return
#             i+=1
#         next=cur2.next
#         cur2.next=None
#         pre.next=reverse(cur1)
#         cur1.next=next
#         pre=cur1
#         cur1=next
#         i=1

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

def reverseK(head,K):
    if head is None or head.next is None or K<2:
        return
    pre=head
    cur1=head.next
    k=1
    while(cur1):
        cur2=cur1
        while(k<K):
            if cur2.next:
                cur2=cur2.next
            else:
                return
            k+=1
        next=cur2.next
        cur2.next=None
        pre.next=reverse(cur1)
        cur1.next=next
        pre=cur1
        cur1=next
        k=1




if __name__ == "__main__":
    head=aux.constructList()
    reverseK(head,2)
    aux.printList(head)





