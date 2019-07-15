class LNode:
    def __init__(self,data=None):
        self.data=data
        self.next=None


"""
函数功能：构造一个含值顺序为1～9的链表
输入参数：无
返回值：该链表的头节点
"""


def constructList(begin,end):
    head=Node()
    cur=head
    i=begin
    while(i<end):
        cur.next=Node(i)
        cur=cur.next
        i+=1
    return head


"""
函数功能：打印链表中的值
输入参数：链表的头节点
返回值：无
"""


def printList(head):
    cur=head.next
    while(cur):
        print(cur.data,end=" ")
        cur=cur.next


'''
树的节点类
'''


class Node():
    def __init__(self,data=None):
        self.data=data
        self.lchild=None
        self.rchild=None


"""
创建二叉树并且实现二叉树的前中后序遍历
"""


def arrayToTree(arr,start,end):
    node=Node()
    if start<=end:
        mid=(start+end+1)//2
        node.data=arr[mid]
        node.lchild=arrayToTree(arr,start,mid-1)
        node.rchild=arrayToTree(arr,mid+1,end)
        return node
    return None


def midOrder(node):
    if node is None:
        return
    midOrder(node.lchild)
    print(node.data,end=" ")
    midOrder(node.rchild)


def pre_order(node):
    if node is None:
        return
    print(node.data,end=" ")
    pre_order(node.lchild)
    pre_order(node.rchild)


def post_order(node):
    if node is None:
        return
    post_order(node.lchild)
    post_order(node.rchild)
    print(node.data,end=" ")

def breath_order(node):
    if node is None:
        return False
    queue=[node]
    while(queue):
        cur=queue.pop(0)
        print(cur.data,end=" ")
        if cur.lchild :
            queue.append(cur.lchild)
        if cur.rchild:
            queue.append(cur.rchild)
