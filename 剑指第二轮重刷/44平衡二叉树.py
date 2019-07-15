# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def IsBalanced_Solution(self, pRoot):
        if not pRoot:
            return True
        return abs(self.get_depth(pRoot.right)-self.get_depth(pRoot.left))<=1

    def get_depth(self,pRoot):
        if not pRoot:
            return 0
        return 1+max(self.get_depth(pRoot.left),self.get_depth(pRoot.right))