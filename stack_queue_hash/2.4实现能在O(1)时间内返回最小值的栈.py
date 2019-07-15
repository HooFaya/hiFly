class Stack:
    def __init__(self):
        self.items=[]
    def isempty(self):
        return len(self.items)==0
    def top(self):
        if self.isempty():
            print("stack is empty")
            return None
        return self.items[len(self.items)-1]
    def push(self,data):
        self.items.append(data)
    def pop(self):
        if self.isempty():
            print("stack is empty")
            return None
        return self.items.pop()

class Mystack():
    def __init__(self):
        #y
        self.itemStack=Stack()
        self.minStack=Stack()
        self.minStack.push(2**32)
    def isempty(self):
        return self.itemStack.isempty()
    def top(self):
        if self.itemStack.isempty():
            print("stack is empty")
        return self.itemStack.top()
    def push(self,data):
        if data<self.minStack.top():
            self.minStack.push(data)
        self.itemStack.push(data)
    def pop(self):
        if self.itemStack.isempty():
            return None
        if self.itemStack.top ==self.minStack.top():
            self.minStack.pop()
        return self.itemStack.pop()
    def getmin(self):
        return self.minStack.top()

def printStack(stack):
    while(not stack.isempty()):
        print(stack.pop(),end=" ")

mystack=Mystack()
mystack.push(1)
mystack.push(2)
mystack.push(3)
printStack(mystack)
print("\n"+str(mystack.getmin()))