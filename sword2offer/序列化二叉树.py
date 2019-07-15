# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def Serialize(self, root):
        self.s = ""
        self.serialize_helper(root)
        return self.s

    def serialize_helper(self, root):
        if root is None:
            self.s += "#,"
            return
        # 注意这里的类型转换，因为是要序列化，所以要转换成字符串
        self.s += str(root.val) + ","
        # if root.left:
        self.serialize_helper(root.left)
        # if root.right:
        self.serialize_helper(root.right)
        # write code here

    def Deserialize(self, s):
        if s is None:
            return None
        self.index = 0
        s = s.split(",")
        return self.Deserialize_helper(s)

    # 编写递归程序时注意，注意函数名字。。。不然debug后发现自己是个傻逼的感觉真难受。。。
    # 为什么要用，分割，因为10和1连在一起变成101，无法分割，所以list(s)千万别用。。。

    def Deserialize_helper(self, s):
        cur_val = s[self.index]
        if cur_val != "#":
            # 注意这里的类型转换，cur_val是字符串，将其初始化为树节点的时候要把它转化为数字
            cur_node = TreeNode(int(cur_val))
            self.index += 1
            cur_node.left = self.Deserialize_helper(s)
            cur_node.right = self.Deserialize_helper(s)
            return cur_node
        else:
            self.index += 1
            return None

        # write code here