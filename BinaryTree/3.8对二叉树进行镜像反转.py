import copy
class Node:
    def __init__(self,data=None):
        self.data=data
        self.lchild=None
        self.rchild=None
def reverse(root):
    if root is None:
        return
    reverse(root.lchild)
    reverse(root.rchild)
    root.lchild,root.rchild=root.rchild,root.lchild

