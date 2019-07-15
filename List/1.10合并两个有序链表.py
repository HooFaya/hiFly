import aux
def merge(h1,h2):
    if h1 is None or h1.next is None:
        return h2
    if h2 is None or h2.next is None:
        return h1
    cur1=h1.next
    cur2=h2.next
    if cur1.data <cur2.data:
        head=h1
        cur=cur1
        cur1=cur1.next
    else:
        head=h2
        cur=cur2
        cur2=cur2.next
    while(cur2 and cur1):
        if cur1.data <cur2.data:
            cur.next=cur1
            cur=cur1
            cur1=cur1.next
        else:
            cur.next=cur2
            cur=cur2
            cur2=cur2.next
    if cur2 is not None:
        cur.next=cur2
    if cur1 is not None:
        cur.next=cur1
    return head
if __name__  =="__main__":
    head1=aux.constructList()
    head2=aux.constructList()
    h=merge(head1,head2)
    aux=aux.printList(h)