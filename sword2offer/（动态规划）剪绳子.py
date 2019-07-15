def f(n):
    """考虑四种特殊情况，0，1，2，3"""
    if n<2:
        return 0
    if n==2:
        return 1
    if n==3:
        return 2
    """这个dp数组存放的是切到第i个位置的最优解"""
    dp=[0]*(n+1)
    dp[0]=0
    dp[1]=1
    dp[2]=2
    dp[3]=3
    for i in range(4,n+1):
        m=0
        for j in range(1,i+1):
            product=dp[j]*dp[i-j]
            if m<product:
                m=product
            dp[i]=m

    return  dp[n]

print(f(8))