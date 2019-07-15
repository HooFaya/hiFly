def delNode(node):
    if node is node.next is None:
        return None
    cur=node
    tmp=cur.next
    cur.data,tmp.data=tmp.data,cur.data
    cur.next=tmp.next



