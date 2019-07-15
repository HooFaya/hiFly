def findPair(arr):
    dict={}
    for i in range(len(arr)):
        j=i+1
        while(j<len(arr)):
            if arr[i]+arr[j] in dict:
                return [(arr[i],arr[j]),(dict[arr[i]+arr[j]])]
            else:
                dict[arr[i]+arr[j]]=(arr[i],arr[j])
            j+=1
    return
print(findPair([3,4,7,10,20,9,8]))