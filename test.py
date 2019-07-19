def heap_sort(arr):
    for i in range((len(arr)-1)//2,-1,-1):
        shift_down(arr,len(arr),i)
    i=len(arr)-1
    while(i>0):
        arr[i],arr[0]=arr[0],arr[i]
        shift_down(arr,i,0)
        i-=1
def shift_down(arr,n,i):
    while(2*i+1<n):
        j=2*i+1
        if j+1<n and arr[j+1]>arr[j]:
            j+=1
        if arr[i]>arr[j]:
            break
        arr[i],arr[j]=arr[j],arr[i]
        i=j
if __name__ == "__main__":
    arr=[5,3,2,1,3,5,3,1]
    heap_sort(arr)
    print(arr,file=open("./res.txt","w"))


