def binary_search(arr,target):
    l=0
    r=len(arr)-1
    while l<=r:
        m=l+(r-l)//2
        if arr[m]==target:
            return m
        elif target<arr[m]:
            r=m-1
        else:
            l=m+1
    return -1
arr=[1,2,233,234,235]
target=233
print(binary_search(arr,target))

