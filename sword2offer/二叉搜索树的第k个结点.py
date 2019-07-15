"""
题目描述
给定一棵二叉搜索树，请找出其中的第k小的结点。
例如,（5，3，7，2，4，6，8中，按结点数值大小顺序第三小结点的值为4。
"""


# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        if k == 0 or pRoot is None:
            return None

        def mid_order(pRoot, res):
            if pRoot.left:
                mid_order(pRoot.left, res)
            res.append(pRoot.val)
            if pRoot.right:
                mid_order(pRoot.right, res)

        res = []
        mid_order(pRoot, res)
        if k > len(res):
            return None
        # 返回的是节点
        return TreeNode(res[k - 1])

    # write code here