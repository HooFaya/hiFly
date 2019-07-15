class Node():
    def __init__(self,data=None):
        self.data=data
        self.lchild=None
        self.rchild=None

def arrayToTree(arr,start,end):
    node=Node()
    if start<=end:
        mid=start+(end-start)//2
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



arr=list(range(1,11))
root=arrayToTree(arr,0,9)
midOrder(root)