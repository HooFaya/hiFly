class Node:
    def __init__(self,data=None):
        self.data=data
        self.lchild=None
        self.rchild=None

def copy_from_tree(root):
    if root is None:
        return None
    dup_root=Node()
    dup_root.data=root.data
    dup_root.lchild=copy_from_tree(root.lchild)
    dup_root.rchild=copy_from_tree(root.rchild)
    return dup_root

#测试案例
t1=Node(1)
t2=Node(2)
t3=Node(3)
t4=Node(4)
t1.lchild=t2
t1.rchild=t3
t2.lchild=t4

def mid_order(root):
    if root is None:
        return
    mid_order(root.lchild)
    print(root.data,end=" ")
    mid_order(root.rchild)
mid_order(t1)

t1_dup=copy_from_tree(t1)
print("\n")
mid_order(t1_dup)











