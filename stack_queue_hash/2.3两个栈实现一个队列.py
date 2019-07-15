class Stack():
    def __init__(self):
        self.items=[]

    def isempty(self):
        return len(self.items)==0

    def top(self):
        if self.isempty():
            return None
        return self.items[len(self.items)-1]

    def push(self,data):
        self.items.append(data)

    def pop(self):
        if self.isempty():
            return None
        return self.items.pop()

class Queue():
    def __init__(self):
        self.stack1=Stack()
        self.stack2=Stack()

    def isempty(self):
        return self.stack1.isempty() and self.stack2.isempty()

    def top(self):
        if self.stack2.isempty():
            self.stack1ToStack2()
        return self.stack2.top()

    def push(self,data):
        self.stack1.push(data)

    def pop(self):
        if self.stack2.isempty():
            self.stack1ToStack2()
        return self.stack2.pop()

    def stack1ToStack2(self):
        if self.stack1.isempty():
            return
        while(not self.stack1.isempty()):
            self.stack2.push(self.stack1.pop())

queue=Queue()
queue.push(1)
queue.push(2)
queue.push(3)
while(not queue.isempty()):
    print(queue.pop(),end=" ")