"""
准备数据
"""
class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def array_to_tree(arr):
    if len(arr)==0:
        return
    mid=len(arr)//2
    root=TreeNode(arr[mid])
    root.left=array_to_tree(arr[:mid])
    root.right=array_to_tree(arr[mid+1:])
    return root

def print_tree(root):
    if not root:
        return
    print_tree(root.left)
    print(root.val,end=" ")
    print_tree(root.right)

root=array_to_tree([1,2,3,4,5,6,7])

"""
树：
               4
            2     6
          1   3  5  7
三种方式，先序，中序，后序
先序为4213657
中序为1234567
后序为1325764
"""


"""先序遍历"""
"""
和层次遍历很像，只不过用到了栈，入栈的时候是先右子树，再左子树
"""
def pre_order(root):
    if not root:
        return
    stack=[root]
    while(stack):
        cur= stack.pop()
        print(cur.val,end=" ")
        if cur.right:
            stack.append(cur.right)
        if cur.left:
            stack.append(cur.left)
print("\n非递归先序遍历为：")
pre_order(root)


"""中序遍历"""
"""将根节点依次压入栈，再判断右子树是否为空"""
def mid_order(root):
    if not root:
        return
    stack=[]
    while(stack or root):
        if root :
            stack.append(root)
            root=root.left
        else:
            root=stack.pop()
            print(root.val,end=" ")
            root=root.right

print("\n非递归中序遍历为")
mid_order(root)


"""后序遍历"""
"""巧用双栈法"""
def post_order(root):
    if not root:
        return
    input=[root]
    output=[]
    while(input):
        cur=input.pop()
        if cur.left:
           input.append(cur.left)
        if cur.right:
            input.append(cur.right)
        output.append(cur)
    while(output):
        cur=output.pop()
        print(cur.val,end=" ")
print("\n非递归后序遍历为：")
post_order(root)

def find_p(root,p1,p2):
    if not root or root is p1 or root is p2:
        return root
    left=find_p(root.left,p1,p2)
    right=find_p(root.right,p1,p2)
    if not left:
        return right
    if not right:
        return left
    return root
def find_pp(root,p1,p2):
    if not root or root is p1 or root is p2:
        return root
    if root.val<p1.val and root.val<p2.val:
        return find_pp(root.right)
    elif root.val>p1.val and root.val>p2.val:
        return find_pp(root.left)
    else:
        return root
