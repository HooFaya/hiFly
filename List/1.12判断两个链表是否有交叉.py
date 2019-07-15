def isCross(head1,head2):
    if head1 is None or head1.next is None or head2 is None or head2.next is None:
        return False
    cur1=head1.next
    cur2=head2.next
    while(cur1.next):
        cur1=cur1.next
    cur1.next=cur2
    fast=head1.next
    slow=head2.next
    while(fast and fast.next):
        fast=fast.next.next
        slow=slow.next
        if fast == slow:
            return True
    return False




