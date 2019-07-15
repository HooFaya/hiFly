'''
    带头节点的链表反转，三指针法
'''
class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None


def reverse(head):
    p=None
    q=head.next
    while(q):
        r=q.next
        q.next=p
        p=q
        q=r
    head.next=p

if __name__ =="__main__":
    head=Node()
    cur=head
    i=1
    while(i <10):
        cur.next=Node(i)
        cur=cur.next
        i+=1

    print("反转之前:")
    cur=head
    while(cur):
        print(cur.data,end=" ")
        tmp=cur
        cur=cur.next

    print("\n反转之后：")
    reverse(head)
    cur=head
    while(cur):
        print(cur.data,end=" ")
        tmp=cur
        cur=cur.next








