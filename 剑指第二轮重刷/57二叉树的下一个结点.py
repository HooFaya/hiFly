# -*- coding:utf-8 -*-
"""
中序遍历的下一个节点
两种情况：
有右子树的情况：返回右子树的最左节点
没右子树的情况：返回当前节点是其父节点的左节点的父节点
"""
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None
class Solution:
    def GetNext(self, pNode):
        if not pNode:
            return
        if pNode.right:
            cur=pNode.right
            while(cur.left):
                cur=cur.left
            return cur
        else:
            while(pNode and pNode.next.left is not pNode):
                pNode=pNode.next
            return pNode.next

