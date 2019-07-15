"""
        后序遍历，根节点在最后被遍历，同时在二叉搜索树中，根节点
的左子树上节点的所有值应当小于根节点的值，右子树应该大于
"""


def is_post_order(arr,left,right):

    if arr is None:
        return False
    base=arr[right]
    i=0
    while(i<right):
        if arr[i]>base:
            break
        i+=1
    j=i

    while(j<right):
        if arr[j]<base:
            return False
        j+=1
#说明当前根节点对左右子树划分的是正确的，即左边的是小于根节点的值，右边是大于根节点的值
    left_flag=True
    right_flag=True

    if (i>left):
        left_flag=is_post_order(arr,left,i-1)
    if (i<right):
        right_flag=is_post_order(arr,i,j-1)
    return left_flag and right_flag

print(is_post_order([1,3,2,5,7,6,4],0,6))




