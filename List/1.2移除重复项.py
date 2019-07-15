'''
要求：
给定一个没有排序的链表
移除链表中的重复项并不改变原顺序

解决办法：
选择排序的思想，略有不同的是：外层单指针，内层双指针
'''
class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None
def removeDup(head):
    if head is None or head.next is None:
        return
    i=head.next
    while(i):
        j=i.next
        k=i
        while(j):
            '''找到重复的节点并删除'''
            if j.data==i.data:
                k.next=j.next
                j=j.next
            else:
                k=j
                j=j.next
        i=i.next
if __name__ == "__main__":
    head=Node()
    i=1
    cur=head
    while(i<10):
        cur.next=Node(i)
        cur=cur.next
        i+=1
    cur.next=Node(6)
    cur.next.next=Node(5)

    print("去重之前：")
    cur = head.next
    while(cur):
        print(cur.data,end=" ")
        cur=cur.next


    print("\n去重之后：")
    removeDup(head)
    cur=head.next
    while(cur):
        print(cur.data,end=" ")
        cur=cur.next












