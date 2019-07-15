import aux

def reverseNeighor(head):
    if head is None or head.next is None:
        return head
    pre=head
    cur=head.next
    while(cur and cur.next):
        next=cur.next.next
        pre.next=cur.next
        cur.next.next=cur
        cur.next=next
        pre=cur
        cur=next
if __name__ =="__main__":
    head=aux.constructList()
    reverseNeighor(head)
    aux.printList(head)