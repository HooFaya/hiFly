def quicksort(arr,start,end):
    if start>=end:
        return
    mid=partsort(arr,start,end)
    quicksort(arr,start,mid)
    quicksort(arr,mid+1,end)


def partsort(arr,start,end):
    base=arr[start]
    while(start<end):
        while(start<end and arr[end]>=base):
            end-=1
        arr[start]=arr[end]
        while (start<end and arr[start]<=base):
            start+=1
        arr[end]=arr[start]
    arr[start]=base
    return start



arr=[4,2,12,4,2,21,42,5]

print(arr)
print("\n快排之后")
quicksort(arr,0,len(arr)-1)
print(arr)






