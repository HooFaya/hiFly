# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def Print(self, pRoot):
        if not pRoot:
            return []
        queue=[pRoot]
        this_level=1
        next_level=0
        res=[]
        tmp=[]
        while(queue):
            cur=queue.pop(0)
            tmp.append(cur.val)
            this_level-=1
            if cur.left:
                queue.append(cur.left)
                next_level+=1
            if cur.right:
                queue.append(cur.right)
                next_level+=1
            if this_level==0:
                res.append(tmp)
                tmp=[]
                this_level=next_level
                next_level=0
        for index,item in enumerate(res):
            if index%2==1:
                item.reverse()
                
        return res





