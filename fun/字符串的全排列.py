def permutation(s):
    def permutation_helper(s,i,res):
        if i==len(s)-1:
            res.append(s[:])
            return
        for j in range(i,len(s)):
            s[i],s[j]=s[j],s[i]
            permutation_helper(s,i+1,res)
            s[j],s[i]=s[i],s[j]

    s=list(s)
    res=[]
    permutation_helper(s,0,res)
    return res


print(permutation("abc"))