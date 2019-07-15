def merge_sort(arr):
    for i in range((len(arr)-1)//2,-1,-1):
        shift_down(arr,len(arr),i)
    for i in range(len(arr)):
        arr[0],arr[-1]=arr[-1],arr[0]
        shift_down(arr,i,0)


def shift_down(arr,n,k):
    while(2*k+1<n):
        j=2*k+1
        if arr[2*k+2]>arr[2*k+1]:
            j+=1
        if arr[k]>arr[j]:
            return
        else:
            arr[k],arr[j]=arr[j],arr[k]
        k=j
arr=[5,4,3,2,1,111]
merge_sort(arr)
print(arr)
def heap_sort(arr):
    #heapify的过程，heapify之后，乱序的数组变成了一个最大堆
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
