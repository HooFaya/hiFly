class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def helper(root,single_path,all_path):
    single_path.append(root.val)

    if root.left is None and root.right is None:
        all_path.append(single_path.copy())
    if root.left is not None:
        helper(root.left, single_path, all_path)
    if root.right is not None:
        helper(root.right,single_path,all_path)

    single_path.pop()




def construct_tree():
    root=Node(6)
    node1=Node(3)
    node2=Node(-7)
    node3=Node(-1)
    node4=Node(9)
    root.left=node1
    root.right=node2
    node1.left=node3
    node1.right=node4
    return root
def find_all_leaf(root,res):

    if root is None:
        return
    if root.left is None and root.right is None:
        res.append(root.val)
    if root.left:
        find_all_leaf(root.left,res)
    if root.right:
        find_all_leaf(root.right,res)


def find_leaf_num(root):
    if root.left is None and root.right is None:
        return 1
    return find_leaf_num(root.left)+find_leaf_num(root.right)

root=construct_tree()

# s_path=[]
# all_path=[]
# helper(root,s_path,all_path)
# print(all_path)


res=[]
find_all_leaf(root,res)
print(res)
print(find_leaf_num(root))
