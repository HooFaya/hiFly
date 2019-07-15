# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def isSymmetrical(self, pRoot):
        self.pre=[]
        self.new=[]
        self.pre_order(pRoot)
        self.new_order(pRoot)
        return self.pre==self.new


    def new_order(self,pRoot):
        if not pRoot:
            self.new.append("#")
            return
        self.new.append(pRoot.val)
        self.new_order(pRoot.right)
        self.new_order(pRoot.left)
    def pre_order(self,pRoot):
        if not pRoot:
            self.pre.append("#")
            return
        self.pre.append(pRoot.val)
        self.pre_order(pRoot.left)
        self.pre_order(pRoot.right)