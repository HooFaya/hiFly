"""
将有序数组转化为一个二叉搜索树，顺便复习3.1
"""
class Node:
    def __init__(self,data=None):
        self.data=data
        self.lchild=None
        self.rchild=None


def array_to_tree(arr,left,right):
    if arr is None:
        return False
    root=Node()

    if (left<=right):
        mid=(left+right+1)//2
        root.data=arr[mid]
        root.lchild=array_to_tree(arr,left,mid-1)
        root.rchild=array_to_tree(arr,mid+1,right)
        return root
    return None

def mid_order(root):
    if root is None:
        return
    mid_order(root.lchild)
    print(root.data,end=" ")
    mid_order(root.rchild)



"""
构造一个栈给下面的程序使用
"""


class Stack:
    def __init__(self):
        self.items=[]

    def isempty(self):
        return len(self.items)==0

    def top(self):
        if self.isempty():
            return None
        return self.items[len(self.items)-1]

    def push(self,item):
        self.items.append(item)

    def pop(self):

        if self.isempty():
            return None
        return self.items.pop()


"""
将某一节点的路径存储到栈中
"""

def findPath(root,node,stack,):
    if node is None:
        return False

    if root is None:
        return False
    if root is node:
        stack.push(root)
        return True
    if findPath(root.lchild,node, stack) or findPath(root.rchild,node,stack):
        stack.push(root)
        return True
    return False


def find_father(root,node1,node2):
    stack1=Stack()
    stack2=Stack()
    findPath(root,node1,stack1)
    findPath(root,node2,stack2)
    while stack1.top() ==stack2.top() :
        common_father=stack1.top()
        stack1.pop()
        stack2.pop()
    return common_father

if __name__ == "__main__":
    arr=list(range(1,11))
    root=array_to_tree(arr,0,len(arr)-1)
    node1=root.lchild.lchild.lchild
    node2=root.lchild.rchild
    father=find_father(root,node1,node2)
    print(father.data)





