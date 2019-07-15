"""
题目描述
从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。
"""
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        #判断特殊情况，判断特殊情况，判断特殊情况
        if pRoot is None:
            return []
        this_level = 1
        next_level = 0
        level_num = 0
        res = [[]]
        if pRoot is None:
            return
        queue = [pRoot]
        while (queue):
            cur = queue.pop(0)
            res[level_num].append(cur.val)
            this_level -= 1
            if cur.left:
                queue.append(cur.left)
                next_level += 1
            if cur.right:
                queue.append(cur.right)
                next_level += 1

            if this_level == 0:
                this_level = next_level
                next_level = 0
                level_num += 1
                res.append([])
        #每一次新的层级，都要加一个[],如果不pop就会多一个空的[]
        res.pop()
        return  res


