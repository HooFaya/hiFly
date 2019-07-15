"""
要求：
给定两个单链表，每个单链表的首节点代表个位数，计算两个链表之和，并以链表方式返回

方法：
链表相加法(整数相加会导致溢出)
"""
class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None


def sum(h1,h2):
    if h1 is None or h1.next is None:
        return h2
    if h2 is None or h2.next is None:
        return h1
    p1=h1.next
    p2=h2.next
    sum=None
    c=0
    tmp=None
    resultNode=Node()
    p=resultNode
    while(p1 and p2):
        sum=p1.data+p2.data+c
        c=sum//10
        tmp=Node()
        tmp.data=sum%10
        p.next=tmp
        p=tmp
        p1=p1.next
        p2=p2.next
    if p1 is None:
        while(p2):
            sum=p2.data+c
            c=sum//10
            tmp=Node()
            tmp.data=sum%10
            p.next=tmp
            p2=p2.next
    if p2 is None:
        while(p1):
            sum=p1.data+c
            c=sum//10
            tmp=Node()
            tmp.data=sum%10
            p.next=tmp
            p1=p1.next
    if c==1:
        tmp=Node()
        tmp.data=c
        p.next=tmp
    return resultNode











if __name__ =="__main__":
    i=1
    head1=Node()
    head1.next=None
    head2=Node()
    head2.next=None
    tmp=None
    cur=head1
    addResult=None
    #构造第一个链表
    while(i<7):
        tmp=Node()
        tmp.data=i+2
        tmp.next=None
        cur.next=tmp
        cur=tmp
        i+=1
    cur=head2
    #构造第二个链表
    i=9
    while(i>4):
        tmp=Node()
        tmp.data=i
        tmp.next=None
        cur.next=tmp
        cur=tmp
        i-=1
    print("\nHead1:")
    cur=head1.next
    while(cur):
        print(cur.data,end=" ")
        cur=cur.next
    print("\nHead2:")
    cur=head2.next
    while(cur):
        print(cur.data,end=" ")
        cur=cur.next
    addResult=sum(head1,head2)
    print("\n相加后：")
    cur=addResult.next
    while(cur):
        print(cur.data,end=" ")
        cur=cur.next














