"""
ps:第一次刷，明确一点：经过某一节点的最大路径和，无外乎四种情况中的最大值
四种情况分别为：
最大值为此节点的本身值（经过左右孩子的最大路径和都为负数）
最大值为此节点的本身值加上左孩子的最大路径和（经过右孩子的最大路径和为负数）
最大值为此节点的本身值加上右孩子的最大路径和（经过左孩子的最大路径和为负数）
最大值为此节点的本身值加上左孩子的最大路径和，再加上左孩子的最大路径和（经过左右孩子的最大路径和都为正数）
在以上四种情况取最大值

"""
# class Intref:
#     def __init__(self, data=None):
#         self.data = data
#
#
# class Node:
#     def __init__(self, data=None):
#         self.data = data
#         self.lchild = None
#         self.rchild = None
#
#
# def helper(root, m):
#     if root is None:
#         return 0
#     else:
#         sumleft = helper(root.lchild, m)
#         sumright = helper(root.rchild, m)
#         tmp = max(root.data, root.data + sumleft, root.data + sumright, root.data + sumright + sumleft)
#         if tmp > m.data:
#             m.data = tmp
#         #返回经过当前节点的最大路径和
#         submax = max(sumleft, sumright,0)
#         return root.data + submax
#
#
#
# def find_max(root):
#     m = Intref()
#     m.data = -2 ** 31
#     helper(root, m)
#     return m.data
"""第二次刷，复现思路"""
class Node:
    def __init__(self,data):
        self.data=data
        self.lchild=None
        self.rchild=None


def find_max(root):
    class IntRef:
        def __init__(self,data=None):
            self.data=data

    def helper(root,max_node):
        if root is None:
            return 0

        left_max=helper(root.lchild,max_node)
        right_max=helper(root.rchild,max_node)
        cur_max=max(root.data,\
                    root.data+left_max,\
                    root.data+right_max,\
                    root.data+left_max+right_max)
        if cur_max>max_node.data:
            max_node.data=cur_max

        sub_max=max(0,left_max,right_max)
        return root.data+sub_max


    max_node=IntRef(-2**31)
    helper(root,max_node)
    return max_node.data

"""测试用例"""
if __name__ == "__main__":
    root = Node(2)
    left = Node(-3)
    right = Node(-5)
    root.lchild = left
    root.rchild = right
    # left.lchild=Node(100)
    # left.rchild=Node(98)
    print(find_max(root))
