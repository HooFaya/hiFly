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
def isPair(seq1,seq2):
    if len(seq1)!=len(seq2):
        return False
    if len(seq1)==0 or len(seq2)==0:
        return False
    stack=Stack()
    i=j=0
    while(i<len(seq1)):
        stack.push(seq1[i])
        i+=1
        while  j<5 and stack.top() ==seq2[j]:
            stack.pop()
            j+=1
    return stack.isempty()
print(isPair([1,2,3,4,5],[3,2,5,4,1]))

