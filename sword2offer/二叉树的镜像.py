# 题目描述
# # 操作给定的二叉树，将其变换为源二叉树的镜像。
# # 输入描述:
# # 二叉树的镜像定义：源二叉树
# #     	    8
# #     	   /  \
# #     	  6   10
# #     	 / \  / \
# #     	5  7 9 11
# #     	镜像二叉树
# #     	    8
# #     	   /  \
# #     	  10   6
# #     	 / \  / \
# #     	11 9 7  5
# -*- coding:utf-8 -*-

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    """
    本题思路：
    如何对一棵树做镜像反转
    递归思路，分两步走
    第一步，先把根节点的左右孩子做镜像翻转
    第二步，再交换两个孩子

    递归结束条件为：
    到了空节点返回
    这个结束条件不能被"到达叶子节点替换"这个结束条件替换
    考虑{8,#,7,#,6,#,5,#,4},没有左孩子，self.Mirror(root.left)执行会报错
    """
    def Mirror(self, root):
        if root is None:
            return
        self.Mirror(root.left)
        self.Mirror(root.right)
        root.left, root.right = root.right, root.left
        return root

