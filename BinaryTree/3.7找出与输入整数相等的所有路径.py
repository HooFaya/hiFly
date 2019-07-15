# 返回二维列表，内部每个列表表示找到的路径
def FindPath(root, expectNumber):
    def helper(root, expectNumber, summer, v, res):
        v.append(root.val)
        summer = sum(v)
        if root.left is None and root.right is None and summer == expectNumber:
            res.append(v.copy())
        if root.left is not None:
            helper(root.left, expectNumber, summer, v, res)
        if root.right is not None:
            helper(root.right, expectNumber, summer, v, res)
        summer -= root.val
        v.pop()

    summer = 0
    v = []
    res = []
    helper(root, expectNumber, summer, v, res)
    return sorted(res, key=lambda x: len(x), reverse=True)


class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def construct_tree():
    root = Node(6)
    node1 = Node(3)
    node2 = Node(-7)
    node3 = Node(-1)
    node4 = Node(9)
    node5 = Node(9)
    root.left = node1
    root.right = node2
    node1.left = node3
    node1.right = node4
    node2.left = node5
    return root




if __name__ == "__main__":
    root = construct_tree()
    print(FindPath(root, 8))
