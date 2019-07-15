def merge_sort(arr):
    if len(arr)==1:
        return arr

    mid=len(arr)//2
    left=merge_sort(arr[:mid])
    right=merge_sort(arr[mid:])
    return merge(left,right)


def merge(left,right):
    if not left:
        return right
    if not right:
        return left
    i,j=0,0
    res=[]
    while(i<len(left) and j<len(right)):
        if left[i]<right[j]:
            res.append(left[i])
            i+=1
        else:
            res.append(right[j])
            j+=1
    res.extend(left[i:])
    res.extend(right[j:])
    return res
print(merge_sort([5,4,2,1,3,4,5]))
