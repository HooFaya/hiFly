'''
方法一：借助一个队列
'''

class Stack():
    def __init__(self):
        self.items=[]
    def isempty(self):
        return len(self.items)==0
    def top(self):
        if self.isempty():
            print("the stack is empty")
            return None
        return self.items[len(self.items)-1]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        if self.isempty():
            print("the stack is empty")
            return None
        return self.items.pop()

def reverseStack(stack):
    queue=[]
    while(not stack.isempty()):
        queue.append(stack.pop())
    while(queue):
        stack.push(queue.pop(0))

def moveBottomToTop(stack):
    if stack.isempty():
        return
    top1=stack.pop()
    if not stack.isempty():
        moveBottomToTop(stack)
        top2=stack.pop()
        stack.push(top1)
        stack.push(top2)
    else:
        stack.push(top1)

if __name__ =="__main__":
    stack=Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
