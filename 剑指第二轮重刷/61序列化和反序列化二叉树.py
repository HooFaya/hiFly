# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def Serialize(self, root):
        if not root:
            return ""
        self.s=""
        self.Serialize_helper(root)
        return self.s
    def Serialize_helper(self,root):
        if not root:
            self.s+="#,"
            return 
        self.s+=str(root.val)+","
        self.Serialize_helper(root.left)
        self.Serialize_helper(root.right)

    def Deserialize(self, s):
        if not s:
            return
        self.index=0
        s=s.split(",")
        return  self.Deserialize_helper(s)

    def Deserialize_helper(self,s):
        if self.index==len(s)-1:
            return None
        cur_val=s[self.index]
        if cur_val == "#":
            self.index+=1
            return None
        cur=TreeNode(int(cur_val))
        self.index+=1
        cur.left=self.Deserialize_helper(s)
        cur.right=self.Deserialize_helper(s)
        return cur




