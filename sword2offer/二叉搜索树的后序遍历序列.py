# -*- coding:utf-8 -*-
"""
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
"""
class Solution:
    """
    思路：利用二叉搜索树的特性，左子树的所有元素都小于等于根，右子树的所有元素都大于等于根
    利用根节点的值将树划分为左右子树，再对左右子树递归的进行判断
    利用两个指针进行判断并划分左右子，即缩小递归的规模
    递归结束条件很重要，细节见代码注释
    """
    def VerifySquenceOfBST(self, sequence):
        if not sequence:
            return False
        # 一个节点的后序遍历就是它本身，所以返回True
        if len(sequence) == 1:
            return True
        root_val = sequence[-1]
        """第一个指针启动，从数组的起始位置开始移动"""
        i = 0
        while (sequence[i] < root_val):
            i += 1
        """移动到第一个大于根值的元素上，第二个指针启动"""
        j = i
        while (j < len(sequence) - 1):
            if sequence[j] < root_val:
                return False
            j += 1
        """至此，左右子树划分完毕，接下来就是递归的判断了"""
        left = True
        right = True
        if (len(sequence[0:i]) > 0):
            left = self.VerifySquenceOfBST(sequence[0:i])
        if (len(sequence[i:j]) > 0):
            #j停在了最后一个元素上，sequence[i:j]刚好不会包括最后一个元素
            right = self.VerifySquenceOfBST(sequence[i:j])
        return left and right

        # write code here