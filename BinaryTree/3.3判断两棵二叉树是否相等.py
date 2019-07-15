def isequal(root1,root2):
    if root1 is  None and root2 is  None:
        return  True
    if root1 is None and root2 is not None:
        return  False
    if root2 is None and root1 is not None:
        return  False
    if root1.data ==root2.data:
        return isequal(root1.lchild,root2.lchild) and isequal(root1.rchild,root2.rchild)
    else:
        return False



import aux
arr=list(range(10))
t1=aux.arrayToTree(arr,0,9)
t2=aux.arrayToTree(arr,0,9)
print(isequal(t1,t2))