# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
思路：
判断B是不是A的子结构，理所当然的：
第一步，先找到具有相同值的根节点，
第二步，顺着相同值的根节点，判断B是不是当前节点的子结构,
如果不是，则在当前节点的左孩子和右孩子重复第一步和第二步
'''

class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if pRoot2 is None:
            return False
        if pRoot1 is None:
            return False
        result = False

        """
        先找到具有相同值的根节点
        顺着相同值的根节点，判断B是不是当前节点的子结构
        """
        if pRoot1.val == pRoot2.val:
            result = self.does_a_has_b(pRoot1, pRoot2)

        """
        如果不是，则在当前节点的左孩子和右孩子重复第一步和第二步
        """
        if not result:
            result = self.HasSubtree(pRoot1.left, pRoot2)
        if not result:
            result = self.HasSubtree(pRoot1.right, pRoot2)
        return result
    def does_a_has_b(self, pRoot1, pRoot2):
        # 如果pRoot2遍历完了，说明pRoot2就是pRoot1的一部分
        if pRoot2 is None:
            return True
        # 如果pRoot1遍历完了，但是pRoot2没有被遍历完，也就是说pRoot2太大了，说明pRoot2不是pRoot1的一部分
        if pRoot1 is None:
            return False
        # 以上是两种递归结束条件，下面进入本轮的判断
        if pRoot1.val != pRoot2.val:
            return False
        return self.does_a_has_b(pRoot1.left, pRoot2.left) and self.does_a_has_b(pRoot1.right, pRoot2.right)




