# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def isSymmetrical(self, pRoot):
        if pRoot is None:
            return True
        self.res1 = []
        self.res2 = []

        # 定义一个新的遍历方式，根右左
        def pre_order(pRoot):
            if pRoot is None:
                # 考虑数字全为一样的情况，所以要把遍历的空节点考虑进去
                self.res1.append("#")
                return
            self.res1.append(pRoot.val)
            pre_order(pRoot.left)
            pre_order(pRoot.right)

        def new_order(pRoot):
            if pRoot is None:
                self.res2.append("#")
                return
            self.res2.append(pRoot.val)
            new_order(pRoot.right)
            new_order(pRoot.left)

        pre_order(pRoot)
        new_order(pRoot)
        return self.res1 == self.res2

        # write code here