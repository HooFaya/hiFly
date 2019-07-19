
def merge_sort(arr):
    for i in range((len(arr)-1)//2,-1,-1):
        shift_down(arr,len(arr),i)
    for i in range(len(arr)):
        arr[0],arr[-1]=arr[-1],arr[0]
        shift_down(arr,i,0)

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

arr=[5,4,3,2,1,111]
merge_sort(arr)
print(arr)
'''
n:需要恢复堆状态的数组元素个数
k:要shift——down的元素位置
'''

