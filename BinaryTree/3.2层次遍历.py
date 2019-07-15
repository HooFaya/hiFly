def breadth_order(root):
    """
    算法题1.1：分层遍历(打印)二叉树
    :param root: 待传入的根节点
    :return: None
    """
    if not root :
        return None
    this_num=1
    next_num=0
    queue=[root]
    while(queue):
        cur=queue.pop(0)
        this_num-=1
        print(cur.val,end=" ")
        if cur.left:
            queue.append(cur.left)
            next_num+=1
        if cur.right:
            queue.append(cur.right)
            next_num+=1
        if this_num==0:
            print("/n")
            this_num=next_num
            next_num=0

def post_order(root):
    """
    算法题1.2：非递归后序遍历二叉树
    :param root: 待传入的根节点
    :return:None
    """
    if not root:
        return
    input=[root]
    output=[]
    while(input):
        cur=input.pop()
        if cur.left:
           input.append(cur.left)
        if cur.right:
            input.append(cur.right)
        output.append(cur)
    while(output):
        cur=output.pop()
        print(cur.val,end=" ")




