class Stack:
    def __init__(self):
        self.itmes=[]
    def push(self,item):
        self.itmes.append(item)
    def top(self):
        if len(self.itmes)==0:
            return None
        return self.itmes[len(self.itmes)-1]
    def pop(self):
        return self.itmes.pop()
    def size(self):
        return len(self.itmes)
    def isepmty(self):
        return len(self.itmes)==0
if __name__ == "__main__":
    s=Stack()
    s.push(4)
    s.push(5)
    print("栈顶元素为:",s.top())
    print("是否为空：" ,s.isepmty())
    print("弹出一个元素后：")
    s.pop()
    print("栈顶元素为:",s.top())
    print("是否为空：" ,s.isepmty())
    print("弹出一个元素后：")
    s.pop()
    print("栈顶元素为:",s.top())
    print("是否为空：" ,s.isepmty())
