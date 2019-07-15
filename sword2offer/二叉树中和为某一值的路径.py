# 题目描述
# 输入一颗二叉树的跟节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
# 路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
# (注意: 在返回值的list中，数组长度大的数组靠前)

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    """
    经典的回溯法题目
    先判断是否符合搜索条件，满足则保存结果复位并退出（注意此题看似没有立即退出实则退出了）
    不满足则继续在左右子树里进行搜索
    """
    def FindPath(self, root, expectNumber):
        if root is None:
            return []

        def helper(root, expectNumber, summer, v, res):
            v.append(root.val)
            summer = sum(v)
            """注意此题看似没有立即退出实则退出了"""
            if root.left is None and root.right is None and summer == expectNumber:
                res.append(v[:])
            if root.left is not None:
                helper(root.left, expectNumber, summer, v, res)
            if root.right is not None:
                helper(root.right, expectNumber, summer, v, res)
            """复位并退出"""
            v.pop()
            summer -= root.val

        summer = 0
        v = []
        res = []
        helper(root, expectNumber, summer, v, res)
        res = sorted(res, key=lambda x: len(x), reverse=True)
        return res

        # write code here