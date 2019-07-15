# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回对应节点TreeNode
    def KthNode(self, pRoot, k):
        if not pRoot:
            return
        self.res=[]
        self.mid_order(pRoot)
        if k<=0 or k>len(self.res):
            return
        return TreeNode(self.res[k-1])
    def mid_order(self,pRoot):
        if not pRoot:
            return
        self.mid_order(pRoot.left)
        self.res.append(pRoot.val)
        self.mid_order(pRoot.right)
