def get_lcs(s1,s2):
    length1=len(s1)
    lenght2=len(s2)
    dp=[[0]*(lenght2+1) for  _ in range(length1+1)]
    maxlen,init=0,0
    for i in range(length1):
        for j in range(lenght2):
            if s1[i]==s2[j]:
                dp[i+1][j+1]=dp[i][j]+1
                if dp[i+1][j+1]>maxlen:
                    maxlen=dp[i+1][j+1]
                    init=i
    return s1[init-maxlen+1:init+1]
print(get_lcs("dasd","dadsdas"))

def get_res(s1):
    length=len(s1)
    dp=[[0]*(length) for _ in range(length)]
    maxLen=0
    init=0
    for j in range(length):
        for i in range(j+1):
            if j-i<2 and s1[i]==s1[j]:
                dp[i][j]=1
            else:
                if s1[i]==s1[j]:
                    dp[i][j]=dp[i+1][j-1]
            if j-i+1>maxLen and dp[i][j]==1:
                maxLen=j-i
                init=i
    return s1[init:init+maxLen+1]

print(get_res("asaadcdaxsasd"))


