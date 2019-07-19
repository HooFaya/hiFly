
def heap_sort(arr):

    #heapify的过程，heapify之后，乱序的数组变成了一个最大堆
    #heapify：从最后的一个非叶子节点开始，向上执行shift_down,

    for i in range((len(arr)-1)//2,-1,-1):
        shift_down(arr,len(arr),i)
    #动态调整的过程，依次将最大的元素放在数组的尾部
    i = len(arr)-1
    while i>0:
    #每次只需要对堆顶进行一次shiftdown，因为是由于交换导致堆顶变化进而变为非最大堆
        arr[0],arr[i]=arr[i],arr[0]
        shift_down(arr,i,0)
        i -= 1
'''
n:需要恢复堆状态的数组元素个数
k:要shift——down的元素位置
'''
def shift_down(arr,n,k):
    #只要有左孩子，就要进行比较
    while 2*k+1<n:
        j=2*k+1
        if j+1<n and arr[j+1]>arr[j]:
            j = j+1
        if arr[k]>arr[j]:
            break
        arr[k],arr[j]=arr[j],arr[k]
        k = j


if __name__ == "__main__":
    arr = [5, 4, 32, 7, 3, 2, 1,1,1]
    heap_sort(arr)
    print(arr)




def shift_down(arr,n,k):
    while(2*k+1<n):
        j=2*k+1
        if arr[j]<arr[j+1]:
            j=j+1
        if arr[k]>arr[j]:
            break
        arr[k],arr[j]=arr[j],arr[k]


class MaxHeap:
    def __init__(self):
        self.heap=["#"]
    def insert(self,item):
        self.shift_up(item)
    def shift_up(self,item):
        self.heap.append(item)
        i=len(self.heap)-1
        while(i>1 and self.heap[i//2]<self.heap[i]):
            self.heap[i//2],self.heap[i]=self.heap[i],self.heap[i//2]
            i=i//2
    def get_item(self):
        if not self.heap:
            return
        self.heap[1],self.heap[-1]=self.heap[-1],self.heap[1]
        res=self.heap.pop()
        k=1
        while(2*k<len(self.heap)):
            j=2*k
            if 2*k+1<len(self.heap):
                if self.heap[2*k]<self.heap[2*k+1]:
                    j=2*k+1
            if self.heap[k]<self.heap[j]:
                self.heap[k],self.heap[j]=self.heap[j],self.heap[k]
                k=j
            else:
                break
        return res

