def bubble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
arr=list(reversed(range(0,10)))
print(arr)
print("\n冒泡之后")
bubble_sort(arr)
print(arr)