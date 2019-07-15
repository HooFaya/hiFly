class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    递归思路：
    先转换左边，
    再把当前节点的左指针指向上一次处理的节点
    再把上一次处理节点的右指针指向当前节点，最后记录本次处理的节点
    后转换右边
    递归出口：遍历到空节点之后退出

    """
    def __init__(self):
        """两个引用分别指向头节点以及上一次处理的节点"""
        self.head=None
        self.end=None
    def Convert(self, pRootOfTree):
        if pRootOfTree is None:
            return
        self.Convert(pRootOfTree.left)
        pRootOfTree.left=self.end
        if self.end is None:
            self.head=pRootOfTree
        else:
            self.end.right=pRootOfTree
        self.end=pRootOfTree
        self.Convert(pRootOfTree.right)
        return self.head


