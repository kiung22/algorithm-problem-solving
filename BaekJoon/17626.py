def f(n):
    dp = [4] * (n+1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n+1):
        s = int((i//4) ** 0.5)
        e = int(i ** 0.5)

        for j in range(s, e+1):
            k = i - j*j
            dp[i] = min(dp[i], dp[k]+1)
    
    return dp[n]


n = int(input())

print(f(n))
