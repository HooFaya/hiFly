
class Solution:
    def Permutation(self, ss):
        def Permutation_helper(ss,res,i):
            if i==len(ss)-1:
                res.append("".join(ss))
                return
            for j in range(i,len(ss)):
                ss[i],ss[j]=ss[j],ss[i]
                Permutation_helper(ss,res,i+1)
                ss[i],ss[j]=ss[j],ss[i]
        ss=list(ss)
        res=[]
        Permutation_helper(ss,res,0)
        return res
s=Solution()
print(s.Permutation("abc"))