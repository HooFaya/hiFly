class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

class Solution:
    #二叉树为BST
    def solution_1(self,root,p1,p2):
        
        if not root or p1 is root or p2 is root:
            return root
        if p1.val<root.val and p2.val<root.val:
            return self.solution_1(root.left,p1,p2)
        if p2.val>root.val and p2.val>root.val:
            return self.solution_1(root.right,p1,p2)
        else:
            return root